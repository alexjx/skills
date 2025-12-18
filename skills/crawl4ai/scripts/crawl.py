#!/usr/bin/env python3
"""Crawl a URL and output markdown content.

Run with: uv run python scripts/crawl.py <url>
"""

import argparse
import asyncio
import sys

from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator


async def crawl(
    url: str,
    include_links: bool = False,
    include_images: bool = False,
    headless: bool = True,
    timeout: int = 30,
) -> str:
    """Crawl URL and return markdown content."""
    browser_config = BrowserConfig(
        browser_type="chromium",
        headless=headless,
    )

    md_generator = DefaultMarkdownGenerator(
        options={
            "ignore_links": not include_links,
            "ignore_images": not include_images,
        }
    )

    run_config = CrawlerRunConfig(
        page_timeout=timeout * 1000,  # ms
        markdown_generator=md_generator,
    )

    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(url=url, config=run_config)

        if not result.success:
            raise RuntimeError(f"Crawl failed: {result.error_message}")

        # result.markdown is MarkdownGenerationResult, access raw_markdown
        if result.markdown:
            return result.markdown.raw_markdown
        return ""


def main():
    parser = argparse.ArgumentParser(
        description="Crawl a URL and convert to markdown"
    )
    parser.add_argument("url", help="URL to crawl")
    parser.add_argument(
        "--output", "-o",
        help="Output file (default: stdout)"
    )
    parser.add_argument(
        "--include-links",
        action="store_true",
        help="Include hyperlinks in output"
    )
    parser.add_argument(
        "--include-images",
        action="store_true",
        help="Include image references in output"
    )
    parser.add_argument(
        "--no-headless",
        action="store_true",
        help="Show browser window"
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=30,
        help="Page load timeout in seconds (default: 30)"
    )

    args = parser.parse_args()

    try:
        markdown = asyncio.run(
            crawl(
                url=args.url,
                include_links=args.include_links,
                include_images=args.include_images,
                headless=not args.no_headless,
                timeout=args.timeout,
            )
        )

        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(markdown)
            print(f"Saved to {args.output}", file=sys.stderr)
        else:
            print(markdown)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
