# Crawl4AI Custom LLM Context
Generated on: 2025-12-18T02:00:15.574Z
Total files: 12
Estimated tokens: 48,459

---

## Installation - Full Content
Component ID: installation
Context Type: memory
Estimated tokens: 1,458

## Installation

Multiple installation options for different environments and use cases.

### Basic Installation

```bash
# Install core library
pip install crawl4ai

# Initial setup (installs Playwright browsers)
crawl4ai-setup

# Verify installation
crawl4ai-doctor
```

### Quick Verification

```python
import asyncio
from crawl4ai import AsyncWebCrawler

async def main():
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun("https://example.com")
        print(result.markdown[:300])

if __name__ == "__main__":
    asyncio.run(main())
```

**📖 Learn more:** [Basic Usage Guide](https://docs.crawl4ai.com/core/quickstart.md)

### Advanced Features (Optional)

```bash
# PyTorch-based features (text clustering, semantic chunking)
pip install crawl4ai[torch]
crawl4ai-setup

# Transformers (Hugging Face models)
pip install crawl4ai[transformer]
crawl4ai-setup

# All features (large download)
pip install crawl4ai[all]
crawl4ai-setup

# Pre-download models (optional)
crawl4ai-download-models
```

**📖 Learn more:** [Advanced Features Documentation](https://docs.crawl4ai.com/extraction/llm-strategies.md)

### Docker Deployment

```bash
# Pull pre-built image (specify platform for consistency)
docker pull --platform linux/amd64 unclecode/crawl4ai:latest
# For ARM (M1/M2 Macs): docker pull --platform linux/arm64 unclecode/crawl4ai:latest

# Setup environment for LLM support
cat > .llm.env << EOL
OPENAI_API_KEY=sk-your-key
ANTHROPIC_API_KEY=your-anthropic-key
EOL

# Run with LLM support (specify platform)
docker run -d \
  --platform linux/amd64 \
  -p 11235:11235 \
  --name crawl4ai \
  --env-file .llm.env \
  --shm-size=1g \
  unclecode/crawl4ai:latest

# For ARM Macs, use: --platform linux/arm64

# Basic run (no LLM)
docker run -d \
  --platform linux/amd64 \
  -p 11235:11235 \
  --name crawl4ai \
  --shm-size=1g \
  unclecode/crawl4ai:latest
```

**📖 Learn more:** [Complete Docker Guide](https://docs.crawl4ai.com/core/docker-deployment.md)

### Docker Compose

```bash
# Clone repository
git clone https://github.com/unclecode/crawl4ai.git
cd crawl4ai

# Copy environment template
cp deploy/docker/.llm.env.example .llm.env
# Edit .llm.env with your API keys

# Run pre-built image
IMAGE=unclecode/crawl4ai:latest docker compose up -d

# Build and run locally
docker compose up --build -d

# Build with all features
INSTALL_TYPE=all docker compose up --build -d

# Stop service
docker compose down
```

**📖 Learn more:** [Docker Compose Configuration](https://docs.crawl4ai.com/core/docker-deployment.md#option-2-using-docker-compose)

### Manual Docker Build

```bash
# Build multi-architecture image (specify platform)
docker buildx build --platform linux/amd64 -t crawl4ai-local:latest --load .
# For ARM: docker buildx build --platform linux/arm64 -t crawl4ai-local:latest --load .

# Build with specific features
docker buildx build \
  --platform linux/amd64 \
  --build-arg INSTALL_TYPE=all \
  --build-arg ENABLE_GPU=false \
  -t crawl4ai-local:latest --load .

# Run custom build (specify platform)
docker run -d \
  --platform linux/amd64 \
  -p 11235:11235 \
  --name crawl4ai-custom \
  --env-file .llm.env \
  --shm-size=1g \
  crawl4ai-local:latest
```

**📖 Learn more:** [Manual Build Guide](https://docs.crawl4ai.com/core/docker-deployment.md#option-3-manual-local-build--run)

### Google Colab

```python
# Install in Colab
!pip install crawl4ai
!crawl4ai-setup

# If setup fails, manually install Playwright browsers
!playwright install chromium

# Install with all features (may take 5-10 minutes)
!pip install crawl4ai[all]
!crawl4ai-setup
!crawl4ai-download-models

# If still having issues, force Playwright install
!playwright install chromium --force

# Quick test
import asyncio
from crawl4ai import AsyncWebCrawler

async def test_crawl():
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun("https://example.com")
        print("✅ Installation successful!")
        print(f"Content length: {len(result.markdown)}")

# Run test in Colab
await test_crawl()
```

**📖 Learn more:** [Colab Examples Notebook](https://colab.research.google.com/github/unclecode/crawl4ai/blob/main/docs/examples/quickstart.ipynb)

### Docker API Usage

```python
# Using Docker SDK
import asyncio
from crawl4ai.docker_client import Crawl4aiDockerClient
from crawl4ai import BrowserConfig, CrawlerRunConfig, CacheMode

async def main():
    async with Crawl4aiDockerClient(base_url="http://localhost:11235") as client:
        results = await client.crawl(
            ["https://example.com"],
            browser_config=BrowserConfig(headless=True),
            crawler_config=CrawlerRunConfig(cache_mode=CacheMode.BYPASS)
        )
        for result in results:
            print(f"Success: {result.success}, Length: {len(result.markdown)}")

asyncio.run(main())
```

**📖 Learn more:** [Docker Client API](https://docs.crawl4ai.com/core/docker-deployment.md#python-sdk)

### Direct API Calls

```python
# REST API example
import requests

payload = {
    "urls": ["https://example.com"],
    "browser_config": {"type": "BrowserConfig", "params": {"headless": True}},
    "crawler_config": {"type": "CrawlerRunConfig", "params": {"cache_mode": "bypass"}}
}

response = requests.post("http://localhost:11235/crawl", json=payload)
print(response.json())
```

**📖 Learn more:** [REST API Reference](https://docs.crawl4ai.com/core/docker-deployment.md#rest-api-examples)

### Health Check

```bash
# Check Docker service
curl http://localhost:11235/health

# Access playground
open http://localhost:11235/playground

# View metrics
curl http://localhost:11235/metrics
```

**📖 Learn more:** [Monitoring & Metrics](https://docs.crawl4ai.com/core/docker-deployment.md#metrics--monitoring)

---


## Installation - Diagrams & Workflows
Component ID: installation
Context Type: reasoning
Estimated tokens: 2,658

## Installation Workflows and Architecture

Visual representations of Crawl4AI installation processes, deployment options, and system interactions.

### Installation Decision Flow

```mermaid
flowchart TD
    A[Start Installation] --> B{Environment Type?}
    
    B -->|Local Development| C[Basic Python Install]
    B -->|Production| D[Docker Deployment]
    B -->|Research/Testing| E[Google Colab]
    B -->|CI/CD Pipeline| F[Automated Setup]
    
    C --> C1[pip install crawl4ai]
    C1 --> C2[crawl4ai-setup]
    C2 --> C3{Need Advanced Features?}
    
    C3 -->|No| C4[Basic Installation Complete]
    C3 -->|Text Clustering| C5[pip install crawl4ai with torch]
    C3 -->|Transformers| C6[pip install crawl4ai with transformer]
    C3 -->|All Features| C7[pip install crawl4ai with all]
    
    C5 --> C8[crawl4ai-download-models]
    C6 --> C8
    C7 --> C8
    C8 --> C9[Advanced Installation Complete]
    
    D --> D1{Deployment Method?}
    D1 -->|Pre-built Image| D2[docker pull unclecode/crawl4ai]
    D1 -->|Docker Compose| D3[Clone repo + docker compose]
    D1 -->|Custom Build| D4[docker buildx build]
    
    D2 --> D5[Configure .llm.env]
    D3 --> D5
    D4 --> D5
    D5 --> D6[docker run with ports]
    D6 --> D7[Docker Deployment Complete]
    
    E --> E1[Colab pip install]
    E1 --> E2[playwright install chromium]
    E2 --> E3[Test basic crawl]
    E3 --> E4[Colab Setup Complete]
    
    F --> F1[Automated pip install]
    F1 --> F2[Automated setup scripts]
    F2 --> F3[CI/CD Integration Complete]
    
    C4 --> G[Verify with crawl4ai-doctor]
    C9 --> G
    D7 --> H[Health check via API]
    E4 --> I[Run test crawl]
    F3 --> G
    
    G --> J[Installation Verified]
    H --> J
    I --> J
    
    style A fill:#e1f5fe
    style J fill:#c8e6c9
    style C4 fill:#fff3e0
    style C9 fill:#fff3e0
    style D7 fill:#f3e5f5
    style E4 fill:#fce4ec
    style F3 fill:#e8f5e8
```

### Basic Installation Sequence

```mermaid
sequenceDiagram
    participant User
    participant PyPI
    participant System
    participant Playwright
    participant Crawler
    
    User->>PyPI: pip install crawl4ai
    PyPI-->>User: Package downloaded
    
    User->>System: crawl4ai-setup
    System->>Playwright: Install browser binaries
    Playwright-->>System: Chromium, Firefox installed
    System-->>User: Setup complete
    
    User->>System: crawl4ai-doctor
    System->>System: Check Python version
    System->>System: Verify Playwright installation
    System->>System: Test browser launch
    System-->>User: Diagnostics report
    
    User->>Crawler: Basic crawl test
    Crawler->>Playwright: Launch browser
    Playwright-->>Crawler: Browser ready
    Crawler->>Crawler: Navigate to test URL
    Crawler-->>User: Success confirmation
```

### Docker Deployment Architecture

```mermaid
graph TB
    subgraph "Host System"
        A[Docker Engine] --> B[Crawl4AI Container]
        C[.llm.env File] --> B
        D[Port 11235] --> B
    end
    
    subgraph "Container Environment"
        B --> E[FastAPI Server]
        B --> F[Playwright Browsers]
        B --> G[Python Runtime]
        
        E --> H[/crawl Endpoint]
        E --> I[/playground Interface]
        E --> J[/health Monitoring]
        E --> K[/metrics Prometheus]
        
        F --> L[Chromium Browser]
        F --> M[Firefox Browser]
        F --> N[WebKit Browser]
    end
    
    subgraph "External Services"
        O[OpenAI API] --> B
        P[Anthropic API] --> B
        Q[Local LLM Ollama] --> B
    end
    
    subgraph "Client Applications"
        R[Python SDK] --> H
        S[REST API Calls] --> H
        T[Web Browser] --> I
        U[Monitoring Tools] --> J
        V[Prometheus] --> K
    end
    
    style B fill:#e3f2fd
    style E fill:#f3e5f5
    style F fill:#e8f5e8
    style G fill:#fff3e0
```

### Advanced Features Installation Flow

```mermaid
stateDiagram-v2
    [*] --> BasicInstall
    
    BasicInstall --> FeatureChoice: crawl4ai installed
    
    FeatureChoice --> TorchInstall: Need text clustering
    FeatureChoice --> TransformerInstall: Need HuggingFace models
    FeatureChoice --> AllInstall: Need everything
    FeatureChoice --> Complete: Basic features sufficient
    
    TorchInstall --> TorchSetup: pip install crawl4ai with torch
    TransformerInstall --> TransformerSetup: pip install crawl4ai with transformer  
    AllInstall --> AllSetup: pip install crawl4ai with all
    
    TorchSetup --> ModelDownload: crawl4ai-setup
    TransformerSetup --> ModelDownload: crawl4ai-setup
    AllSetup --> ModelDownload: crawl4ai-setup
    
    ModelDownload --> PreDownload: crawl4ai-download-models
    PreDownload --> Complete: All models cached
    
    Complete --> Verification: crawl4ai-doctor
    Verification --> [*]: Installation verified
    
    note right of TorchInstall : PyTorch for semantic operations
    note right of TransformerInstall : HuggingFace for LLM features
    note right of AllInstall : Complete feature set
```

### Platform-Specific Installation Matrix

```mermaid
graph LR
    subgraph "Installation Methods"
        A[Python Package] --> A1[pip install]
        B[Docker Image] --> B1[docker pull]
        C[Source Build] --> C1[git clone + build]
        D[Cloud Platform] --> D1[Colab/Kaggle]
    end
    
    subgraph "Operating Systems"
        E[Linux x86_64]
        F[Linux ARM64] 
        G[macOS Intel]
        H[macOS Apple Silicon]
        I[Windows x86_64]
    end
    
    subgraph "Feature Sets"
        J[Basic crawling]
        K[Text clustering torch]
        L[LLM transformers]
        M[All features]
    end
    
    A1 --> E
    A1 --> F
    A1 --> G
    A1 --> H
    A1 --> I
    
    B1 --> E
    B1 --> F
    B1 --> G
    B1 --> H
    
    C1 --> E
    C1 --> F
    C1 --> G
    C1 --> H
    C1 --> I
    
    D1 --> E
    D1 --> I
    
    E --> J
    E --> K
    E --> L
    E --> M
    
    F --> J
    F --> K
    F --> L
    F --> M
    
    G --> J
    G --> K
    G --> L
    G --> M
    
    H --> J
    H --> K
    H --> L
    H --> M
    
    I --> J
    I --> K
    I --> L
    I --> M
    
    style A1 fill:#e3f2fd
    style B1 fill:#f3e5f5
    style C1 fill:#e8f5e8
    style D1 fill:#fff3e0
```

### Docker Multi-Stage Build Process

```mermaid
sequenceDiagram
    participant Dev as Developer
    participant Git as GitHub Repo
    participant Docker as Docker Engine
    participant Registry as Docker Hub
    participant User as End User
    
    Dev->>Git: Push code changes
    
    Docker->>Git: Clone repository
    Docker->>Docker: Stage 1 - Base Python image
    Docker->>Docker: Stage 2 - Install dependencies
    Docker->>Docker: Stage 3 - Install Playwright
    Docker->>Docker: Stage 4 - Copy application code
    Docker->>Docker: Stage 5 - Setup FastAPI server
    
    Note over Docker: Multi-architecture build
    Docker->>Docker: Build for linux/amd64
    Docker->>Docker: Build for linux/arm64
    
    Docker->>Registry: Push multi-arch manifest
    Registry-->>Docker: Build complete
    
    User->>Registry: docker pull unclecode/crawl4ai
    Registry-->>User: Download appropriate architecture
    
    User->>Docker: docker run with configuration
    Docker->>Docker: Start container
    Docker->>Docker: Initialize FastAPI server
    Docker->>Docker: Setup Playwright browsers
    Docker-->>User: Service ready on port 11235
```

### Installation Verification Workflow

```mermaid
flowchart TD
    A[Installation Complete] --> B[Run crawl4ai-doctor]
    
    B --> C{Python Version Check}
    C -->|✓ 3.10+| D{Playwright Check}
    C -->|✗ < 3.10| C1[Upgrade Python]
    C1 --> D
    
    D -->|✓ Installed| E{Browser Binaries}
    D -->|✗ Missing| D1[Run crawl4ai-setup]
    D1 --> E
    
    E -->|✓ Available| F{Test Browser Launch}
    E -->|✗ Missing| E1[playwright install]
    E1 --> F
    
    F -->|✓ Success| G[Test Basic Crawl]
    F -->|✗ Failed| F1[Check system dependencies]
    F1 --> F
    
    G --> H{Crawl Test Result}
    H -->|✓ Success| I[Installation Verified ✓]
    H -->|✗ Failed| H1[Check network/permissions]
    H1 --> G
    
    I --> J[Ready for Production Use]
    
    style I fill:#c8e6c9
    style J fill:#e8f5e8
    style C1 fill:#ffcdd2
    style D1 fill:#fff3e0
    style E1 fill:#fff3e0
    style F1 fill:#ffcdd2
    style H1 fill:#ffcdd2
```

### Resource Requirements by Installation Type

```mermaid
graph TD
    subgraph "Basic Installation"
        A1[Memory: 512MB]
        A2[Disk: 2GB]
        A3[CPU: 1 core]
        A4[Network: Required for setup]
    end
    
    subgraph "Advanced Features torch"
        B1[Memory: 2GB+]
        B2[Disk: 5GB+]
        B3[CPU: 2+ cores]
        B4[GPU: Optional CUDA]
    end
    
    subgraph "All Features"
        C1[Memory: 4GB+]
        C2[Disk: 10GB+]
        C3[CPU: 4+ cores]
        C4[GPU: Recommended]
    end
    
    subgraph "Docker Deployment"
        D1[Memory: 1GB+]
        D2[Disk: 3GB+]
        D3[CPU: 2+ cores]
        D4[Ports: 11235]
        D5[Shared Memory: 1GB]
    end
    
    style A1 fill:#e8f5e8
    style B1 fill:#fff3e0
    style C1 fill:#ffecb3
    style D1 fill:#e3f2fd
```

**📖 Learn more:** [Installation Guide](https://docs.crawl4ai.com/core/installation/), [Docker Deployment](https://docs.crawl4ai.com/core/docker-deployment/), [System Requirements](https://docs.crawl4ai.com/core/installation/#prerequisites)

---


## Simple Crawling - Full Content
Component ID: simple_crawling
Context Type: memory
Estimated tokens: 2,390

## Simple Crawling

Basic web crawling operations with AsyncWebCrawler, configurations, and response handling.

### Basic Setup

```python
import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig

async def main():
    browser_config = BrowserConfig()  # Default browser settings
    run_config = CrawlerRunConfig()   # Default crawl settings

    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(
            url="https://example.com",
            config=run_config
        )
        print(result.markdown)

if __name__ == "__main__":
    asyncio.run(main())
```

### Understanding CrawlResult

```python
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
from crawl4ai.content_filter_strategy import PruningContentFilter

config = CrawlerRunConfig(
    markdown_generator=DefaultMarkdownGenerator(
        content_filter=PruningContentFilter(threshold=0.6),
        options={"ignore_links": True}
    )
)

result = await crawler.arun("https://example.com", config=config)

# Different content formats
print(result.html)                    # Raw HTML
print(result.cleaned_html)            # Cleaned HTML  
print(result.markdown.raw_markdown)   # Raw markdown
print(result.markdown.fit_markdown)   # Filtered markdown

# Status information
print(result.success)      # True/False
print(result.status_code)  # HTTP status (200, 404, etc.)

# Extracted content
print(result.media)        # Images, videos, audio
print(result.links)        # Internal/external links
```

### Basic Configuration Options

```python
run_config = CrawlerRunConfig(
    word_count_threshold=10,        # Min words per block
    exclude_external_links=True,    # Remove external links
    remove_overlay_elements=True,   # Remove popups/modals
    process_iframes=True,           # Process iframe content
    excluded_tags=['form', 'header']  # Skip these tags
)

result = await crawler.arun("https://example.com", config=run_config)
```

### Error Handling

```python
result = await crawler.arun("https://example.com", config=run_config)

if not result.success:
    print(f"Crawl failed: {result.error_message}")
    print(f"Status code: {result.status_code}")
else:
    print(f"Success! Content length: {len(result.markdown)}")
```

### Debugging with Verbose Logging

```python
browser_config = BrowserConfig(verbose=True)

async with AsyncWebCrawler(config=browser_config) as crawler:
    result = await crawler.arun("https://example.com")
    # Detailed logging output will be displayed
```

### Complete Example

```python
import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode

async def comprehensive_crawl():
    browser_config = BrowserConfig(verbose=True)
    
    run_config = CrawlerRunConfig(
        # Content filtering
        word_count_threshold=10,
        excluded_tags=['form', 'header', 'nav'],
        exclude_external_links=True,
        
        # Content processing
        process_iframes=True,
        remove_overlay_elements=True,
        
        # Cache control
        cache_mode=CacheMode.ENABLED
    )

    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(
            url="https://example.com",
            config=run_config
        )
        
        if result.success:
            # Display content summary
            print(f"Title: {result.metadata.get('title', 'No title')}")
            print(f"Content: {result.markdown[:500]}...")
            
            # Process media
            images = result.media.get("images", [])
            print(f"Found {len(images)} images")
            for img in images[:3]:  # First 3 images
                print(f"  - {img.get('src', 'No src')}")
            
            # Process links
            internal_links = result.links.get("internal", [])
            print(f"Found {len(internal_links)} internal links")
            for link in internal_links[:3]:  # First 3 links
                print(f"  - {link.get('href', 'No href')}")
                
        else:
            print(f"❌ Crawl failed: {result.error_message}")
            print(f"Status: {result.status_code}")

if __name__ == "__main__":
    asyncio.run(comprehensive_crawl())
```

### Working with Raw HTML and Local Files

```python
# Crawl raw HTML
raw_html = "<html><body><h1>Test</h1><p>Content</p></body></html>"
result = await crawler.arun(f"raw://{raw_html}")

# Crawl local file
result = await crawler.arun("file:///path/to/local/file.html")

# Both return standard CrawlResult objects
print(result.markdown)
```

## Table Extraction

Extract structured data from HTML tables with automatic detection and scoring.

### Basic Table Extraction

```python
import asyncio
import pandas as pd
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode

async def extract_tables():
    async with AsyncWebCrawler() as crawler:
        config = CrawlerRunConfig(
            table_score_threshold=7,  # Higher = stricter detection
            cache_mode=CacheMode.BYPASS
        )
        
        result = await crawler.arun("https://example.com/tables", config=config)
        
        if result.success and result.tables:
            # New tables field (v0.6+)
            for i, table in enumerate(result.tables):
                print(f"Table {i+1}:")
                print(f"Headers: {table['headers']}")
                print(f"Rows: {len(table['rows'])}")
                print(f"Caption: {table.get('caption', 'No caption')}")
                
                # Convert to DataFrame
                df = pd.DataFrame(table['rows'], columns=table['headers'])
                print(df.head())

asyncio.run(extract_tables())
```

### Advanced Table Processing

```python
from crawl4ai import LXMLWebScrapingStrategy

async def process_financial_tables():
    config = CrawlerRunConfig(
        table_score_threshold=8,  # Strict detection for data tables
        scraping_strategy=LXMLWebScrapingStrategy(),
        keep_data_attributes=True,
        scan_full_page=True
    )
    
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun("https://coinmarketcap.com", config=config)
        
        if result.tables:
            # Get the main data table (usually first/largest)
            main_table = result.tables[0]
            
            # Create DataFrame
            df = pd.DataFrame(
                main_table['rows'],
                columns=main_table['headers']
            )
            
            # Clean and process data
            df = clean_financial_data(df)
            
            # Save for analysis
            df.to_csv("market_data.csv", index=False)
            return df

def clean_financial_data(df):
    """Clean currency symbols, percentages, and large numbers"""
    for col in df.columns:
        if 'price' in col.lower():
            # Remove currency symbols
            df[col] = df[col].str.replace(r'[^\d.]', '', regex=True)
            df[col] = pd.to_numeric(df[col], errors='coerce')
        
        elif '%' in str(df[col].iloc[0]):
            # Convert percentages
            df[col] = df[col].str.replace('%', '').astype(float) / 100
        
        elif any(suffix in str(df[col].iloc[0]) for suffix in ['B', 'M', 'K']):
            # Handle large numbers (Billions, Millions, etc.)
            df[col] = df[col].apply(convert_large_numbers)
    
    return df

def convert_large_numbers(value):
    """Convert 1.5B -> 1500000000"""
    if pd.isna(value):
        return float('nan')
    
    value = str(value)
    multiplier = 1
    if 'B' in value:
        multiplier = 1e9
    elif 'M' in value:
        multiplier = 1e6
    elif 'K' in value:
        multiplier = 1e3
    
    number = float(re.sub(r'[^\d.]', '', value))
    return number * multiplier
```

### Table Detection Configuration

```python
# Strict table detection (data-heavy pages)
strict_config = CrawlerRunConfig(
    table_score_threshold=9,  # Only high-quality tables
    word_count_threshold=5,   # Ignore sparse content
    excluded_tags=['nav', 'footer']  # Skip navigation tables
)

# Lenient detection (mixed content pages)
lenient_config = CrawlerRunConfig(
    table_score_threshold=5,  # Include layout tables
    process_iframes=True,     # Check embedded tables
    scan_full_page=True      # Scroll to load dynamic tables
)

# Financial/data site optimization
financial_config = CrawlerRunConfig(
    table_score_threshold=8,
    scraping_strategy=LXMLWebScrapingStrategy(),
    wait_for="css:table",     # Wait for tables to load
    scan_full_page=True,
    scroll_delay=0.2
)
```

### Multi-Table Processing

```python
async def extract_all_tables():
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun("https://example.com/data", config=config)
        
        tables_data = {}
        
        for i, table in enumerate(result.tables):
            # Create meaningful names based on content
            table_name = (
                table.get('caption') or 
                f"table_{i+1}_{table['headers'][0]}"
            ).replace(' ', '_').lower()
            
            df = pd.DataFrame(table['rows'], columns=table['headers'])
            
            # Store with metadata
            tables_data[table_name] = {
                'dataframe': df,
                'headers': table['headers'],
                'row_count': len(table['rows']),
                'caption': table.get('caption'),
                'summary': table.get('summary')
            }
        
        return tables_data

# Usage
tables = await extract_all_tables()
for name, data in tables.items():
    print(f"{name}: {data['row_count']} rows")
    data['dataframe'].to_csv(f"{name}.csv")
```

### Backward Compatibility

```python
# Support both new and old table formats
def get_tables(result):
    # New format (v0.6+)
    if hasattr(result, 'tables') and result.tables:
        return result.tables
    
    # Fallback to media.tables (older versions)
    return result.media.get('tables', [])

# Usage in existing code
result = await crawler.arun(url, config=config)
tables = get_tables(result)

for table in tables:
    df = pd.DataFrame(table['rows'], columns=table['headers'])
    # Process table data...
```

### Table Quality Scoring

```python
# Understanding table_score_threshold values:
# 10: Only perfect data tables (headers + data rows)
# 8-9: High-quality tables (recommended for financial/data sites)
# 6-7: Mixed content tables (news sites, wikis)
# 4-5: Layout tables included (broader detection)
# 1-3: All table-like structures (very permissive)

config = CrawlerRunConfig(
    table_score_threshold=8,  # Balanced detection
    verbose=True  # See scoring details in logs
)
```


**📖 Learn more:** [CrawlResult API Reference](https://docs.crawl4ai.com/api/crawl-result/), [Browser & Crawler Configuration](https://docs.crawl4ai.com/core/browser-crawler-config/), [Cache Modes](https://docs.crawl4ai.com/core/cache-modes/)

---


## Simple Crawling - Diagrams & Workflows
Component ID: simple_crawling
Context Type: reasoning
Estimated tokens: 3,133

## Simple Crawling Workflows and Data Flow

Visual representations of basic web crawling operations, configuration patterns, and result processing workflows.

### Basic Crawling Sequence

```mermaid
sequenceDiagram
    participant User
    participant Crawler as AsyncWebCrawler
    participant Browser as Browser Instance
    participant Page as Web Page
    participant Processor as Content Processor
    
    User->>Crawler: Create with BrowserConfig
    Crawler->>Browser: Launch browser instance
    Browser-->>Crawler: Browser ready
    
    User->>Crawler: arun(url, CrawlerRunConfig)
    Crawler->>Browser: Create new page/context
    Browser->>Page: Navigate to URL
    Page-->>Browser: Page loaded
    
    Browser->>Processor: Extract raw HTML
    Processor->>Processor: Clean HTML
    Processor->>Processor: Generate markdown
    Processor->>Processor: Extract media/links
    Processor-->>Crawler: CrawlResult created
    
    Crawler-->>User: Return CrawlResult
    
    Note over User,Processor: All processing happens asynchronously
```

### Crawling Configuration Flow

```mermaid
flowchart TD
    A[Start Crawling] --> B{Browser Config Set?}
    
    B -->|No| B1[Use Default BrowserConfig]
    B -->|Yes| B2[Custom BrowserConfig]
    
    B1 --> C[Launch Browser]
    B2 --> C
    
    C --> D{Crawler Run Config Set?}
    
    D -->|No| D1[Use Default CrawlerRunConfig]
    D -->|Yes| D2[Custom CrawlerRunConfig]
    
    D1 --> E[Navigate to URL]
    D2 --> E
    
    E --> F{Page Load Success?}
    F -->|No| F1[Return Error Result]
    F -->|Yes| G[Apply Content Filters]
    
    G --> G1{excluded_tags set?}
    G1 -->|Yes| G2[Remove specified tags]
    G1 -->|No| G3[Keep all tags]
    G2 --> G4{css_selector set?}
    G3 --> G4
    
    G4 -->|Yes| G5[Extract selected elements]
    G4 -->|No| G6[Process full page]
    G5 --> H[Generate Markdown]
    G6 --> H
    
    H --> H1{markdown_generator set?}
    H1 -->|Yes| H2[Use custom generator]
    H1 -->|No| H3[Use default generator]
    H2 --> I[Extract Media and Links]
    H3 --> I
    
    I --> I1{process_iframes?}
    I1 -->|Yes| I2[Include iframe content]
    I1 -->|No| I3[Skip iframes]
    I2 --> J[Create CrawlResult]
    I3 --> J
    
    J --> K[Return Result]
    
    style A fill:#e1f5fe
    style K fill:#c8e6c9
    style F1 fill:#ffcdd2
```

### CrawlResult Data Structure

```mermaid
graph TB
    subgraph "CrawlResult Object"
        A[CrawlResult] --> B[Basic Info]
        A --> C[Content Variants]
        A --> D[Extracted Data]
        A --> E[Media Assets]
        A --> F[Optional Outputs]
        
        B --> B1[url: Final URL]
        B --> B2[success: Boolean]
        B --> B3[status_code: HTTP Status]
        B --> B4[error_message: Error Details]
        
        C --> C1[html: Raw HTML]
        C --> C2[cleaned_html: Sanitized HTML]
        C --> C3[markdown: MarkdownGenerationResult]
        
        C3 --> C3A[raw_markdown: Basic conversion]
        C3 --> C3B[markdown_with_citations: With references]
        C3 --> C3C[fit_markdown: Filtered content]
        C3 --> C3D[references_markdown: Citation list]
        
        D --> D1[links: Internal/External]
        D --> D2[media: Images/Videos/Audio]
        D --> D3[metadata: Page info]
        D --> D4[extracted_content: JSON data]
        D --> D5[tables: Structured table data]
        
        E --> E1[screenshot: Base64 image]
        E --> E2[pdf: PDF bytes]
        E --> E3[mhtml: Archive file]
        E --> E4[downloaded_files: File paths]
        
        F --> F1[session_id: Browser session]
        F --> F2[ssl_certificate: Security info]
        F --> F3[response_headers: HTTP headers]
        F --> F4[network_requests: Traffic log]
        F --> F5[console_messages: Browser logs]
    end
    
    style A fill:#e3f2fd
    style C3 fill:#f3e5f5
    style D5 fill:#e8f5e8
```

### Content Processing Pipeline

```mermaid
flowchart LR
    subgraph "Input Sources"
        A1[Web URL]
        A2[Raw HTML]
        A3[Local File]
    end
    
    A1 --> B[Browser Navigation]
    A2 --> C[Direct Processing]
    A3 --> C
    
    B --> D[Raw HTML Capture]
    C --> D
    
    D --> E{Content Filtering}
    
    E --> E1[Remove Scripts/Styles]
    E --> E2[Apply excluded_tags]
    E --> E3[Apply css_selector]
    E --> E4[Remove overlay elements]
    
    E1 --> F[Cleaned HTML]
    E2 --> F
    E3 --> F
    E4 --> F
    
    F --> G{Markdown Generation}
    
    G --> G1[HTML to Markdown]
    G --> G2[Apply Content Filter]
    G --> G3[Generate Citations]
    
    G1 --> H[MarkdownGenerationResult]
    G2 --> H
    G3 --> H
    
    F --> I{Media Extraction}
    I --> I1[Find Images]
    I --> I2[Find Videos/Audio]
    I --> I3[Score Relevance]
    I1 --> J[Media Dictionary]
    I2 --> J
    I3 --> J
    
    F --> K{Link Extraction}
    K --> K1[Internal Links]
    K --> K2[External Links]
    K --> K3[Apply Link Filters]
    K1 --> L[Links Dictionary]
    K2 --> L
    K3 --> L
    
    H --> M[Final CrawlResult]
    J --> M
    L --> M
    
    style D fill:#e3f2fd
    style F fill:#f3e5f5
    style H fill:#e8f5e8
    style M fill:#c8e6c9
```

### Table Extraction Workflow

```mermaid
stateDiagram-v2
    [*] --> DetectTables
    
    DetectTables --> ScoreTables: Find table elements
    
    ScoreTables --> EvaluateThreshold: Calculate quality scores
    EvaluateThreshold --> PassThreshold: score >= table_score_threshold
    EvaluateThreshold --> RejectTable: score < threshold
    
    PassThreshold --> ExtractHeaders: Parse table structure
    ExtractHeaders --> ExtractRows: Get header cells
    ExtractRows --> ExtractMetadata: Get data rows
    ExtractMetadata --> CreateTableObject: Get caption/summary
    
    CreateTableObject --> AddToResult: {headers, rows, caption, summary}
    AddToResult --> [*]: Table extraction complete
    
    RejectTable --> [*]: Table skipped
    
    note right of ScoreTables : Factors: header presence, data density, structure quality
    note right of EvaluateThreshold : Threshold 1-10, higher = stricter
```

### Error Handling Decision Tree

```mermaid
flowchart TD
    A[Start Crawl] --> B[Navigate to URL]
    
    B --> C{Navigation Success?}
    C -->|Network Error| C1[Set error_message: Network failure]
    C -->|Timeout| C2[Set error_message: Page timeout]
    C -->|Invalid URL| C3[Set error_message: Invalid URL format]
    C -->|Success| D[Process Page Content]
    
    C1 --> E[success = False]
    C2 --> E
    C3 --> E
    
    D --> F{Content Processing OK?}
    F -->|Parser Error| F1[Set error_message: HTML parsing failed]
    F -->|Memory Error| F2[Set error_message: Insufficient memory]
    F -->|Success| G[Generate Outputs]
    
    F1 --> E
    F2 --> E
    
    G --> H{Output Generation OK?}
    H -->|Markdown Error| H1[Partial success with warnings]
    H -->|Extraction Error| H2[Partial success with warnings]
    H -->|Success| I[success = True]
    
    H1 --> I
    H2 --> I
    
    E --> J[Return Failed CrawlResult]
    I --> K[Return Successful CrawlResult]
    
    J --> L[User Error Handling]
    K --> M[User Result Processing]
    
    L --> L1{Check error_message}
    L1 -->|Network| L2[Retry with different config]
    L1 -->|Timeout| L3[Increase page_timeout]
    L1 -->|Parser| L4[Try different scraping_strategy]
    
    style E fill:#ffcdd2
    style I fill:#c8e6c9
    style J fill:#ffcdd2
    style K fill:#c8e6c9
```

### Configuration Impact Matrix

```mermaid
graph TB
    subgraph "Configuration Categories"
        A[Content Processing]
        B[Page Interaction] 
        C[Output Generation]
        D[Performance]
    end
    
    subgraph "Configuration Options"
        A --> A1[word_count_threshold]
        A --> A2[excluded_tags]
        A --> A3[css_selector]
        A --> A4[exclude_external_links]
        
        B --> B1[process_iframes]
        B --> B2[remove_overlay_elements]
        B --> B3[scan_full_page]
        B --> B4[wait_for]
        
        C --> C1[screenshot]
        C --> C2[pdf] 
        C --> C3[markdown_generator]
        C --> C4[table_score_threshold]
        
        D --> D1[cache_mode]
        D --> D2[verbose]
        D --> D3[page_timeout]
        D --> D4[semaphore_count]
    end
    
    subgraph "Result Impact"
        A1 --> R1[Filters short text blocks]
        A2 --> R2[Removes specified HTML tags]
        A3 --> R3[Focuses on selected content]
        A4 --> R4[Cleans links dictionary]
        
        B1 --> R5[Includes iframe content]
        B2 --> R6[Removes popups/modals]
        B3 --> R7[Loads dynamic content]
        B4 --> R8[Waits for specific elements]
        
        C1 --> R9[Adds screenshot field]
        C2 --> R10[Adds pdf field]
        C3 --> R11[Custom markdown processing]
        C4 --> R12[Filters table quality]
        
        D1 --> R13[Controls caching behavior]
        D2 --> R14[Detailed logging output]
        D3 --> R15[Prevents timeout errors]
        D4 --> R16[Limits concurrent operations]
    end
    
    style A fill:#e3f2fd
    style B fill:#f3e5f5
    style C fill:#e8f5e8
    style D fill:#fff3e0
```

### Raw HTML and Local File Processing

```mermaid
sequenceDiagram
    participant User
    participant Crawler
    participant Processor
    participant FileSystem
    
    Note over User,FileSystem: Raw HTML Processing
    User->>Crawler: arun("raw://html_content")
    Crawler->>Processor: Parse raw HTML directly
    Processor->>Processor: Apply same content filters
    Processor-->>Crawler: Standard CrawlResult
    Crawler-->>User: Result with markdown
    
    Note over User,FileSystem: Local File Processing  
    User->>Crawler: arun("file:///path/to/file.html")
    Crawler->>FileSystem: Read local file
    FileSystem-->>Crawler: File content
    Crawler->>Processor: Process file HTML
    Processor->>Processor: Apply content processing
    Processor-->>Crawler: Standard CrawlResult
    Crawler-->>User: Result with markdown
    
    Note over User,FileSystem: Both return identical CrawlResult structure
```

### Comprehensive Processing Example Flow

```mermaid
flowchart TD
    A[Input: example.com] --> B[Create Configurations]
    
    B --> B1[BrowserConfig verbose=True]
    B --> B2[CrawlerRunConfig with filters]
    
    B1 --> C[Launch AsyncWebCrawler]
    B2 --> C
    
    C --> D[Navigate and Process]
    
    D --> E{Check Success}
    E -->|Failed| E1[Print Error Message]
    E -->|Success| F[Extract Content Summary]
    
    F --> F1[Get Page Title]
    F --> F2[Get Content Preview]
    F --> F3[Process Media Items]
    F --> F4[Process Links]
    
    F3 --> F3A[Count Images]
    F3 --> F3B[Show First 3 Images]
    
    F4 --> F4A[Count Internal Links]
    F4 --> F4B[Show First 3 Links]
    
    F1 --> G[Display Results]
    F2 --> G
    F3A --> G
    F3B --> G
    F4A --> G
    F4B --> G
    
    E1 --> H[End with Error]
    G --> I[End with Success]
    
    style E1 fill:#ffcdd2
    style G fill:#c8e6c9
    style H fill:#ffcdd2
    style I fill:#c8e6c9
```

**📖 Learn more:** [Simple Crawling Guide](https://docs.crawl4ai.com/core/simple-crawling/), [Configuration Options](https://docs.crawl4ai.com/core/browser-crawler-config/), [Result Processing](https://docs.crawl4ai.com/core/crawler-result/), [Table Extraction](https://docs.crawl4ai.com/extraction/no-llm-strategies/)

---


## Configuration Objects - Full Content
Component ID: config_objects
Context Type: memory
Estimated tokens: 7,868

## Browser, Crawler & LLM Configuration

Core configuration classes for controlling browser behavior, crawl operations, LLM providers, and understanding crawl results.

### BrowserConfig - Browser Environment Setup

```python
from crawl4ai import BrowserConfig, AsyncWebCrawler

# Basic browser configuration
browser_config = BrowserConfig(
    browser_type="chromium",  # "chromium", "firefox", "webkit"
    headless=True,           # False for visible browser (debugging)
    viewport_width=1280,
    viewport_height=720,
    verbose=True
)

# Advanced browser setup with proxy and persistence
browser_config = BrowserConfig(
    headless=False,
    proxy="http://user:pass@proxy:8080",
    use_persistent_context=True,
    user_data_dir="./browser_data",
    cookies=[
        {"name": "session", "value": "abc123", "domain": "example.com"}
    ],
    headers={"Accept-Language": "en-US,en;q=0.9"},
    user_agent="Mozilla/5.0 (X11; Linux x86_64) Chrome/116.0.0.0 Safari/537.36",
    text_mode=True,  # Disable images for faster crawling
    extra_args=["--disable-extensions", "--no-sandbox"]
)

async with AsyncWebCrawler(config=browser_config) as crawler:
    result = await crawler.arun("https://example.com")
```

### CrawlerRunConfig - Crawl Operation Control

```python
from crawl4ai import CrawlerRunConfig, CacheMode
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
from crawl4ai.content_filter_strategy import PruningContentFilter

# Basic crawl configuration
run_config = CrawlerRunConfig(
    cache_mode=CacheMode.BYPASS,
    word_count_threshold=10,
    excluded_tags=["nav", "footer", "script"],
    exclude_external_links=True,
    screenshot=True,
    pdf=True
)

# Advanced content processing
md_generator = DefaultMarkdownGenerator(
    content_filter=PruningContentFilter(threshold=0.6),
    options={"citations": True, "ignore_links": False}
)

run_config = CrawlerRunConfig(
    # Content processing
    markdown_generator=md_generator,
    css_selector="main.content",  # Focus on specific content
    target_elements=[".article", ".post"],  # Multiple target selectors
    process_iframes=True,
    remove_overlay_elements=True,
    
    # Page interaction
    js_code=[
        "window.scrollTo(0, document.body.scrollHeight);",
        "document.querySelector('.load-more')?.click();"
    ],
    wait_for="css:.content-loaded",
    wait_for_timeout=10000,
    scan_full_page=True,
    
    # Session management
    session_id="persistent_session",
    
    # Media handling
    screenshot=True,
    pdf=True,
    capture_mhtml=True,
    image_score_threshold=5,
    
    # Advanced options
    simulate_user=True,
    magic=True,  # Auto-handle popups
    verbose=True
)
```

### CrawlerRunConfig Parameters by Category

```python
# Content Processing
config = CrawlerRunConfig(
    word_count_threshold=10,              # Min words per content block
    css_selector="main.article",          # Focus on specific content
    target_elements=[".post", ".content"], # Multiple target selectors
    excluded_tags=["nav", "footer"],       # Remove these tags
    excluded_selector="#ads, .tracker",   # Remove by selector
    only_text=True,                       # Text-only extraction
    keep_data_attributes=True,            # Preserve data-* attributes
    remove_forms=True,                    # Remove all forms
    process_iframes=True                  # Include iframe content
)

# Page Navigation & Timing
config = CrawlerRunConfig(
    wait_until="networkidle",             # Wait condition
    page_timeout=60000,                   # 60 second timeout
    wait_for="css:.loaded",               # Wait for specific element
    wait_for_images=True,                 # Wait for images to load
    delay_before_return_html=0.5,         # Final delay before capture
    semaphore_count=10                    # Max concurrent operations
)

# Page Interaction
config = CrawlerRunConfig(
    js_code="document.querySelector('button').click();",
    scan_full_page=True,                  # Auto-scroll page
    scroll_delay=0.3,                     # Delay between scrolls
    remove_overlay_elements=True,         # Remove popups/modals
    simulate_user=True,                   # Simulate human behavior
    override_navigator=True,              # Override navigator properties
    magic=True                           # Auto-handle common patterns
)

# Caching & Session
config = CrawlerRunConfig(
    cache_mode=CacheMode.BYPASS,          # Cache behavior
    session_id="my_session",              # Persistent session
    shared_data={"context": "value"}      # Share data between hooks
)

# Media & Output
config = CrawlerRunConfig(
    screenshot=True,                      # Capture screenshot
    pdf=True,                            # Generate PDF
    capture_mhtml=True,                  # Capture MHTML archive
    image_score_threshold=3,             # Filter low-quality images
    exclude_external_images=True         # Remove external images
)

# Link & Domain Filtering
config = CrawlerRunConfig(
    exclude_external_links=True,         # Remove external links
    exclude_social_media_links=True,     # Remove social media links
    exclude_domains=["ads.com", "tracker.io"],  # Custom domain filter
    exclude_internal_links=False         # Keep internal links
)
```

### LLMConfig - Language Model Setup

```python
from crawl4ai import LLMConfig

# OpenAI configuration
llm_config = LLMConfig(
    provider="openai/gpt-4o-mini",
    api_token=os.getenv("OPENAI_API_KEY"),  # or "env:OPENAI_API_KEY"
    temperature=0.1,
    max_tokens=2000
)

# Local model with Ollama
llm_config = LLMConfig(
    provider="ollama/llama3.3",
    api_token=None,  # Not needed for Ollama
    base_url="http://localhost:11434"  # Custom endpoint
)

# Anthropic Claude
llm_config = LLMConfig(
    provider="anthropic/claude-3-5-sonnet-20240620",
    api_token="env:ANTHROPIC_API_KEY",
    max_tokens=4000
)

# Google Gemini
llm_config = LLMConfig(
    provider="gemini/gemini-1.5-pro",
    api_token="env:GEMINI_API_KEY"
)

# Groq (fast inference)
llm_config = LLMConfig(
    provider="groq/llama3-70b-8192",
    api_token="env:GROQ_API_KEY"
)
```

### CrawlResult - Understanding Output

```python
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig

async with AsyncWebCrawler() as crawler:
    result = await crawler.arun("https://example.com", config=run_config)
    
    # Basic status information
    print(f"Success: {result.success}")
    print(f"Status: {result.status_code}")
    print(f"URL: {result.url}")
    
    if not result.success:
        print(f"Error: {result.error_message}")
        return
    
    # HTML content variants
    print(f"Original HTML: {len(result.html)} chars")
    print(f"Cleaned HTML: {len(result.cleaned_html or '')} chars")
    
    # Markdown output (MarkdownGenerationResult)
    if result.markdown:
        print(f"Raw markdown: {len(result.markdown.raw_markdown)} chars")
        print(f"With citations: {len(result.markdown.markdown_with_citations)} chars")
        
        # Filtered content (if content filter was used)
        if result.markdown.fit_markdown:
            print(f"Fit markdown: {len(result.markdown.fit_markdown)} chars")
            print(f"Fit HTML: {len(result.markdown.fit_html)} chars")
    
    # Extracted structured data
    if result.extracted_content:
        import json
        data = json.loads(result.extracted_content)
        print(f"Extracted {len(data)} items")
    
    # Media and links
    images = result.media.get("images", [])
    print(f"Found {len(images)} images")
    for img in images[:3]:  # First 3 images
        print(f"  {img.get('src')} (score: {img.get('score', 0)})")
    
    internal_links = result.links.get("internal", [])
    external_links = result.links.get("external", [])
    print(f"Links: {len(internal_links)} internal, {len(external_links)} external")
    
    # Generated files
    if result.screenshot:
        print(f"Screenshot captured: {len(result.screenshot)} chars (base64)")
        # Save screenshot
        import base64
        with open("page.png", "wb") as f:
            f.write(base64.b64decode(result.screenshot))
    
    if result.pdf:
        print(f"PDF generated: {len(result.pdf)} bytes")
        with open("page.pdf", "wb") as f:
            f.write(result.pdf)
    
    if result.mhtml:
        print(f"MHTML captured: {len(result.mhtml)} chars")
        with open("page.mhtml", "w", encoding="utf-8") as f:
            f.write(result.mhtml)
    
    # SSL certificate information
    if result.ssl_certificate:
        print(f"SSL Issuer: {result.ssl_certificate.issuer}")
        print(f"Valid until: {result.ssl_certificate.valid_until}")
    
    # Network and console data (if captured)
    if result.network_requests:
        requests = [r for r in result.network_requests if r.get("event_type") == "request"]
        print(f"Network requests captured: {len(requests)}")
    
    if result.console_messages:
        errors = [m for m in result.console_messages if m.get("type") == "error"]
        print(f"Console messages: {len(result.console_messages)} ({len(errors)} errors)")
    
    # Session and metadata
    if result.session_id:
        print(f"Session ID: {result.session_id}")
    
    if result.metadata:
        print(f"Metadata: {result.metadata.get('title', 'No title')}")
```

### Configuration Helpers and Best Practices

```python
# Clone configurations for variations
base_config = CrawlerRunConfig(
    cache_mode=CacheMode.ENABLED,
    word_count_threshold=200,
    verbose=True
)

# Create streaming version
stream_config = base_config.clone(
    stream=True,
    cache_mode=CacheMode.BYPASS
)

# Create debug version
debug_config = base_config.clone(
    headless=False,
    page_timeout=120000,
    verbose=True
)

# Serialize/deserialize configurations
config_dict = base_config.dump()  # Convert to dict
restored_config = CrawlerRunConfig.load(config_dict)  # Restore from dict

# Browser configuration management
browser_config = BrowserConfig(headless=True, text_mode=True)
browser_dict = browser_config.to_dict()
cloned_browser = browser_config.clone(headless=False, verbose=True)
```

### Common Configuration Patterns

```python
# Fast text-only crawling
fast_config = CrawlerRunConfig(
    cache_mode=CacheMode.ENABLED,
    text_mode=True,
    exclude_external_links=True,
    exclude_external_images=True,
    word_count_threshold=50
)

# Comprehensive data extraction
comprehensive_config = CrawlerRunConfig(
    process_iframes=True,
    scan_full_page=True,
    wait_for_images=True,
    screenshot=True,
    capture_network_requests=True,
    capture_console_messages=True,
    magic=True
)

# Stealth crawling
stealth_config = CrawlerRunConfig(
    simulate_user=True,
    override_navigator=True,
    mean_delay=2.0,
    max_range=1.0,
    user_agent_mode="random"
)
```

### Advanced Configuration Features

#### User Agent Management & Bot Detection Avoidance

```python
from crawl4ai import CrawlerRunConfig

# Random user agent generation
config = CrawlerRunConfig(
    user_agent_mode="random",
    user_agent_generator_config={
        "platform": "windows",  # "windows", "macos", "linux", "android", "ios"
        "browser": "chrome",    # "chrome", "firefox", "safari", "edge"
        "device_type": "desktop"  # "desktop", "mobile", "tablet"
    }
)

# Custom user agent with stealth features
config = CrawlerRunConfig(
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    simulate_user=True,      # Simulate human mouse movements
    override_navigator=True,  # Override navigator properties
    mean_delay=1.5,          # Random delays between actions
    max_range=2.0
)

# Combined anti-detection approach
stealth_config = CrawlerRunConfig(
    user_agent_mode="random",
    simulate_user=True,
    override_navigator=True,
    magic=True,  # Auto-handle common bot detection patterns
    delay_before_return_html=2.0
)
```

#### Proxy Configuration with ProxyConfig

```python
from crawl4ai import CrawlerRunConfig, ProxyConfig, ProxyRotationStrategy

# Single proxy configuration
proxy_config = ProxyConfig(
    server="http://proxy.example.com:8080",
    username="proxy_user",
    password="proxy_pass"
)

# From proxy string format
proxy_config = ProxyConfig.from_string("192.168.1.100:8080:username:password")

# Multiple proxies with rotation
proxies = [
    ProxyConfig(server="http://proxy1.com:8080", username="user1", password="pass1"),
    ProxyConfig(server="http://proxy2.com:8080", username="user2", password="pass2"),
    ProxyConfig(server="http://proxy3.com:8080", username="user3", password="pass3")
]

rotation_strategy = ProxyRotationStrategy(
    proxies=proxies,
    rotation_method="round_robin"  # or "random", "least_used"
)

config = CrawlerRunConfig(
    proxy_config=proxy_config,
    proxy_rotation_strategy=rotation_strategy
)

# Load proxies from environment variable
proxies_from_env = ProxyConfig.from_env("MY_PROXIES")  # comma-separated proxy strings
```

#### Content Selection: css_selector vs target_elements

```python
from crawl4ai import CrawlerRunConfig

# css_selector: Extracts HTML at top level, affects entire processing
config = CrawlerRunConfig(
    css_selector="main.article, .content-area",  # Can be list of selectors
    # Everything else (markdown, extraction, links) works only on this HTML subset
)

# target_elements: Focuses extraction within already processed HTML
config = CrawlerRunConfig(
    css_selector="body",  # First extract entire body
    target_elements=[     # Then focus extraction on these elements
        ".article-content",
        ".post-body", 
        ".main-text"
    ],
    # Links, media from entire body, but markdown/extraction only from target_elements
)

# Hierarchical content selection
config = CrawlerRunConfig(
    css_selector=["#main-content", ".article-wrapper"],  # Top-level extraction
    target_elements=[                                     # Subset for processing
        ".article-title",
        ".article-body", 
        ".article-metadata"
    ],
    excluded_selector="#sidebar, .ads, .comments"  # Remove these from selection
)
```

#### Advanced wait_for Conditions

```python
from crawl4ai import CrawlerRunConfig

# CSS selector waiting
config = CrawlerRunConfig(
    wait_for="css:.content-loaded",  # Wait for element to appear
    wait_for_timeout=15000
)

# JavaScript boolean expression waiting
config = CrawlerRunConfig(
    wait_for="js:() => window.dataLoaded === true",  # Custom JS condition
    wait_for_timeout=20000
)

# Complex JavaScript conditions
config = CrawlerRunConfig(
    wait_for="js:() => document.querySelectorAll('.item').length >= 10",
    js_code=[
        "document.querySelector('.load-more')?.click();",
        "window.scrollTo(0, document.body.scrollHeight);"
    ]
)

# Multiple conditions with JavaScript
config = CrawlerRunConfig(
    wait_for="js:() => !document.querySelector('.loading') && document.querySelector('.results')",
    page_timeout=30000
)
```

#### Session Management for Multi-Step Crawling

```python
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode

# Persistent session across multiple arun() calls
async def multi_step_crawling():
    async with AsyncWebCrawler() as crawler:
        # Step 1: Login page
        login_config = CrawlerRunConfig(
            session_id="user_session",  # Create persistent session
            js_code="document.querySelector('#username').value = 'user'; document.querySelector('#password').value = 'pass'; document.querySelector('#login').click();",
            wait_for="css:.dashboard",
            cache_mode=CacheMode.BYPASS
        )
        
        result1 = await crawler.arun("https://example.com/login", config=login_config)
        
        # Step 2: Navigate to protected area (reuses same browser page)
        nav_config = CrawlerRunConfig(
            session_id="user_session",  # Same session = same browser page
            js_only=True,  # No page reload, just JS navigation
            js_code="window.location.href = '/dashboard/data';",
            wait_for="css:.data-table"
        )
        
        result2 = await crawler.arun("https://example.com/dashboard/data", config=nav_config)
        
        # Step 3: Extract data from multiple pages
        for page in range(1, 6):
            page_config = CrawlerRunConfig(
                session_id="user_session",
                js_only=True,
                js_code=f"document.querySelector('.page-{page}').click();",
                wait_for=f"js:() => document.querySelector('.page-{page}').classList.contains('active')"
            )
            
            result = await crawler.arun(f"https://example.com/data/page/{page}", config=page_config)
            print(f"Page {page} data extracted: {len(result.extracted_content)}")
        
        # Important: Kill session when done
        await crawler.kill_session("user_session")

# Session with shared data between steps
async def session_with_shared_data():
    shared_context = {"user_id": "12345", "preferences": {"theme": "dark"}}
    
    config = CrawlerRunConfig(
        session_id="persistent_session",
        shared_data=shared_context,  # Available across all session calls
        js_code="console.log('User ID:', window.sharedData.user_id);"
    )
```

#### Identity-Based Crawling Parameters

```python
from crawl4ai import CrawlerRunConfig, GeolocationConfig

# Locale and timezone simulation
config = CrawlerRunConfig(
    locale="en-US",                    # Browser language preference
    timezone_id="America/New_York",    # Timezone setting
    user_agent_mode="random",
    user_agent_generator_config={
        "platform": "windows",
        "locale": "en-US"
    }
)

# Geolocation simulation
geo_config = GeolocationConfig(
    latitude=40.7128,   # New York coordinates
    longitude=-74.0060,
    accuracy=100.0
)

config = CrawlerRunConfig(
    geolocation=geo_config,
    locale="en-US",
    timezone_id="America/New_York"
)

# Complete identity simulation
identity_config = CrawlerRunConfig(
    # Location identity
    locale="fr-FR",
    timezone_id="Europe/Paris", 
    geolocation=GeolocationConfig(latitude=48.8566, longitude=2.3522),
    
    # Browser identity
    user_agent_mode="random",
    user_agent_generator_config={
        "platform": "windows",
        "locale": "fr-FR",
        "browser": "chrome"
    },
    
    # Behavioral identity
    simulate_user=True,
    override_navigator=True,
    mean_delay=2.0,
    max_range=1.5
)
```

#### Simplified Import Pattern

```python
# Almost everything from crawl4ai main package
from crawl4ai import (
    AsyncWebCrawler,
    BrowserConfig, 
    CrawlerRunConfig,
    LLMConfig,
    CacheMode,
    ProxyConfig,
    GeolocationConfig
)

# Specialized strategies (still from crawl4ai)
from crawl4ai import (
    JsonCssExtractionStrategy,
    LLMExtractionStrategy,
    DefaultMarkdownGenerator,
    PruningContentFilter,
    RegexChunking
)

# Complete example with simplified imports
async def example_crawl():
    browser_config = BrowserConfig(headless=True)
    
    run_config = CrawlerRunConfig(
        user_agent_mode="random",
        proxy_config=ProxyConfig.from_string("192.168.1.1:8080:user:pass"),
        css_selector="main.content",
        target_elements=[".article", ".post"],
        wait_for="js:() => document.querySelector('.loaded')",
        session_id="my_session",
        simulate_user=True
    )
    
    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun("https://example.com", config=run_config)
        return result
```

## Advanced Features

Comprehensive guide to advanced crawling capabilities including file handling, authentication, dynamic content, monitoring, and session management.

### File Download Handling

```python
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
import os

# Enable downloads with custom path
downloads_path = os.path.join(os.getcwd(), "my_downloads")
os.makedirs(downloads_path, exist_ok=True)

browser_config = BrowserConfig(
    accept_downloads=True,
    downloads_path=downloads_path
)

# Trigger downloads with JavaScript
async def download_files():
    async with AsyncWebCrawler(config=browser_config) as crawler:
        config = CrawlerRunConfig(
            js_code="""
                // Click download links
                const downloadLinks = document.querySelectorAll('a[href$=".pdf"]');
                for (const link of downloadLinks) {
                    link.click();
                    await new Promise(r => setTimeout(r, 2000));  // Delay between downloads
                }
            """,
            wait_for=5  # Wait for downloads to start
        )
        
        result = await crawler.arun("https://example.com/downloads", config=config)
        
        if result.downloaded_files:
            print("Downloaded files:")
            for file_path in result.downloaded_files:
                print(f"- {file_path} ({os.path.getsize(file_path)} bytes)")
```

### Hooks & Authentication

```python
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
from playwright.async_api import Page, BrowserContext

async def advanced_crawler_with_hooks():
    browser_config = BrowserConfig(headless=True, verbose=True)
    crawler = AsyncWebCrawler(config=browser_config)

    # Hook functions for different stages
    async def on_browser_created(browser, **kwargs):
        print("[HOOK] Browser created successfully")
        return browser

    async def on_page_context_created(page: Page, context: BrowserContext, **kwargs):
        print("[HOOK] Setting up page & context")
        
        # Block images for faster crawling
        async def route_filter(route):
            if route.request.resource_type == "image":
                await route.abort()
            else:
                await route.continue_()
        
        await context.route("**", route_filter)
        
        # Simulate login if needed
        # await page.goto("https://example.com/login")
        # await page.fill("input[name='username']", "testuser")
        # await page.fill("input[name='password']", "password123")
        # await page.click("button[type='submit']")
        
        await page.set_viewport_size({"width": 1080, "height": 600})
        return page

    async def before_goto(page: Page, context: BrowserContext, url: str, **kwargs):
        print(f"[HOOK] About to navigate to: {url}")
        await page.set_extra_http_headers({"Custom-Header": "my-value"})
        return page

    async def after_goto(page: Page, context: BrowserContext, url: str, response, **kwargs):
        print(f"[HOOK] Successfully loaded: {url}")
        try:
            await page.wait_for_selector('.content', timeout=1000)
            print("[HOOK] Content found!")
        except:
            print("[HOOK] Content not found, continuing")
        return page

    async def before_retrieve_html(page: Page, context: BrowserContext, **kwargs):
        print("[HOOK] Final actions before HTML retrieval")
        await page.evaluate("window.scrollTo(0, document.body.scrollHeight);")
        return page

    # Attach hooks
    crawler.crawler_strategy.set_hook("on_browser_created", on_browser_created)
    crawler.crawler_strategy.set_hook("on_page_context_created", on_page_context_created)
    crawler.crawler_strategy.set_hook("before_goto", before_goto)
    crawler.crawler_strategy.set_hook("after_goto", after_goto)
    crawler.crawler_strategy.set_hook("before_retrieve_html", before_retrieve_html)

    await crawler.start()
    
    config = CrawlerRunConfig()
    result = await crawler.arun("https://example.com", config=config)
    
    if result.success:
        print(f"Crawled successfully: {len(result.html)} chars")
    
    await crawler.close()
```

### Lazy Loading & Dynamic Content

```python
# Handle lazy-loaded images and infinite scroll
async def handle_lazy_loading():
    config = CrawlerRunConfig(
        # Wait for images to fully load
        wait_for_images=True,
        
        # Automatically scroll entire page to trigger lazy loading
        scan_full_page=True,
        scroll_delay=0.5,  # Delay between scroll steps
        
        # JavaScript for custom lazy loading
        js_code="""
            // Scroll and wait for content to load
            window.scrollTo(0, document.body.scrollHeight);
            
            // Click "Load More" if available
            const loadMoreBtn = document.querySelector('.load-more');
            if (loadMoreBtn) {
                loadMoreBtn.click();
            }
        """,
        
        # Wait for specific content to appear
        wait_for="css:.lazy-content:nth-child(20)",  # Wait for 20 items
        
        # Exclude external images to focus on main content
        exclude_external_images=True
    )
    
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun("https://example.com/gallery", config=config)
        
        if result.success:
            images = result.media.get("images", [])
            print(f"Loaded {len(images)} images after lazy loading")
            for img in images[:3]:
                print(f"- {img.get('src')} (score: {img.get('score', 'N/A')})")
```

### Network & Console Monitoring

```python
# Capture all network requests and console messages for debugging
async def monitor_network_and_console():
    config = CrawlerRunConfig(
        capture_network_requests=True,
        capture_console_messages=True
    )
    
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun("https://example.com", config=config)
        
        if result.success:
            # Analyze network requests
            if result.network_requests:
                requests = [r for r in result.network_requests if r.get("event_type") == "request"]
                responses = [r for r in result.network_requests if r.get("event_type") == "response"]
                failures = [r for r in result.network_requests if r.get("event_type") == "request_failed"]
                
                print(f"Network activity: {len(requests)} requests, {len(responses)} responses, {len(failures)} failures")
                
                # Find API calls
                api_calls = [r for r in requests if "api" in r.get("url", "")]
                print(f"API calls detected: {len(api_calls)}")
                
                # Show failed requests
                for failure in failures[:3]:
                    print(f"Failed: {failure.get('url')} - {failure.get('failure_text')}")
            
            # Analyze console messages
            if result.console_messages:
                message_types = {}
                for msg in result.console_messages:
                    msg_type = msg.get("type", "unknown")
                    message_types[msg_type] = message_types.get(msg_type, 0) + 1
                
                print(f"Console messages: {message_types}")
                
                # Show errors
                errors = [msg for msg in result.console_messages if msg.get("type") == "error"]
                for error in errors[:2]:
                    print(f"JS Error: {error.get('text', '')[:100]}")
```

### Session Management for Multi-Step Workflows

```python
# Maintain state across multiple requests for complex workflows
async def multi_step_session_workflow():
    session_id = "workflow_session"
    
    async with AsyncWebCrawler() as crawler:
        # Step 1: Initial page load
        config1 = CrawlerRunConfig(
            session_id=session_id,
            wait_for="css:.content-loaded"
        )
        
        result1 = await crawler.arun("https://example.com/step1", config=config1)
        print("Step 1 completed")
        
        # Step 2: Navigate and interact (same browser tab)
        config2 = CrawlerRunConfig(
            session_id=session_id,
            js_only=True,  # Don't reload page, just run JS
            js_code="""
                document.querySelector('#next-button').click();
            """,
            wait_for="css:.step2-content"
        )
        
        result2 = await crawler.arun("https://example.com/step2", config=config2)
        print("Step 2 completed")
        
        # Step 3: Form submission
        config3 = CrawlerRunConfig(
            session_id=session_id,
            js_only=True,
            js_code="""
                document.querySelector('#form-field').value = 'test data';
                document.querySelector('#submit-btn').click();
            """,
            wait_for="css:.results"
        )
        
        result3 = await crawler.arun("https://example.com/submit", config=config3)
        print("Step 3 completed")
        
        # Clean up session
        await crawler.crawler_strategy.kill_session(session_id)

# Advanced GitHub commits pagination example
async def github_commits_pagination():
    session_id = "github_session"
    all_commits = []
    
    async with AsyncWebCrawler() as crawler:
        for page in range(3):
            if page == 0:
                # Initial load
                config = CrawlerRunConfig(
                    session_id=session_id,
                    wait_for="js:() => document.querySelectorAll('li.Box-sc-g0xbh4-0').length > 0"
                )
            else:
                # Navigate to next page
                config = CrawlerRunConfig(
                    session_id=session_id,
                    js_only=True,
                    js_code='document.querySelector(\'a[data-testid="pagination-next-button"]\').click();',
                    wait_for="js:() => document.querySelectorAll('li.Box-sc-g0xbh4-0').length > 0"
                )
            
            result = await crawler.arun(
                "https://github.com/microsoft/TypeScript/commits/main",
                config=config
            )
            
            if result.success:
                commit_count = result.cleaned_html.count('li.Box-sc-g0xbh4-0')
                print(f"Page {page + 1}: Found {commit_count} commits")
        
        await crawler.crawler_strategy.kill_session(session_id)
```

### SSL Certificate Analysis

```python
# Fetch and analyze SSL certificates
async def analyze_ssl_certificates():
    config = CrawlerRunConfig(
        fetch_ssl_certificate=True
    )
    
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun("https://example.com", config=config)
        
        if result.success and result.ssl_certificate:
            cert = result.ssl_certificate
            
            # Basic certificate info
            print(f"Issuer: {cert.issuer.get('CN', 'Unknown')}")
            print(f"Subject: {cert.subject.get('CN', 'Unknown')}")
            print(f"Valid from: {cert.valid_from}")
            print(f"Valid until: {cert.valid_until}")
            print(f"Fingerprint: {cert.fingerprint}")
            
            # Export certificate in different formats
            import os
            os.makedirs("certificates", exist_ok=True)
            
            cert.to_json("certificates/cert.json")
            cert.to_pem("certificates/cert.pem")
            cert.to_der("certificates/cert.der")
            
            print("Certificate exported in multiple formats")
```

### Advanced Page Interaction

```python
# Complex page interactions with dynamic content
async def advanced_page_interaction():
    async with AsyncWebCrawler() as crawler:
        # Multi-step interaction with waiting
        config = CrawlerRunConfig(
            js_code=[
                # Step 1: Scroll to load content
                "window.scrollTo(0, document.body.scrollHeight);",
                
                # Step 2: Wait and click load more
                """
                (async () => {
                    await new Promise(resolve => setTimeout(resolve, 2000));
                    const loadMore = document.querySelector('.load-more');
                    if (loadMore) loadMore.click();
                })();
                """
            ],
            
            # Wait for new content to appear
            wait_for="js:() => document.querySelectorAll('.item').length > 20",
            
            # Additional timing controls
            page_timeout=60000,  # 60 second timeout
            delay_before_return_html=2.0,  # Wait before final capture
            
            # Handle overlays automatically
            remove_overlay_elements=True,
            magic=True,  # Auto-handle common popup patterns
            
            # Simulate human behavior
            simulate_user=True,
            override_navigator=True
        )
        
        result = await crawler.arun("https://example.com/dynamic", config=config)
        
        if result.success:
            print(f"Interactive crawl completed: {len(result.cleaned_html)} chars")

# Form interaction example
async def form_interaction_example():
    config = CrawlerRunConfig(
        js_code="""
            // Fill search form
            document.querySelector('#search-input').value = 'machine learning';
            document.querySelector('#category-select').value = 'technology';
            document.querySelector('#search-form').submit();
        """,
        wait_for="css:.search-results",
        session_id="search_session"
    )
    
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun("https://example.com/search", config=config)
        print("Search completed, results loaded")
```

### Local File & Raw HTML Processing

```python
# Handle different input types: URLs, local files, raw HTML
async def handle_different_inputs():
    async with AsyncWebCrawler() as crawler:
        # 1. Regular web URL
        result1 = await crawler.arun("https://example.com")
        
        # 2. Local HTML file
        local_file_path = "/path/to/file.html"
        result2 = await crawler.arun(f"file://{local_file_path}")
        
        # 3. Raw HTML content
        raw_html = "<html><body><h1>Test Content</h1><p>Sample text</p></body></html>"
        result3 = await crawler.arun(f"raw:{raw_html}")
        
        # All return the same CrawlResult structure
        for i, result in enumerate([result1, result2, result3], 1):
            if result.success:
                print(f"Input {i}: {len(result.markdown)} chars of markdown")

# Save and re-process HTML example
async def save_and_reprocess():
    async with AsyncWebCrawler() as crawler:
        # Original crawl
        result = await crawler.arun("https://example.com")
        
        if result.success:
            # Save HTML to file
            with open("saved_page.html", "w", encoding="utf-8") as f:
                f.write(result.html)
            
            # Re-process from file
            file_result = await crawler.arun("file://./saved_page.html")
            
            # Process as raw HTML
            raw_result = await crawler.arun(f"raw:{result.html}")
            
            # Verify consistency
            assert len(result.markdown) == len(file_result.markdown) == len(raw_result.markdown)
            print("✅ All processing methods produced identical results")
```

### Advanced Link & Media Handling

```python
# Comprehensive link and media extraction with filtering
async def advanced_link_media_handling():
    config = CrawlerRunConfig(
        # Link filtering
        exclude_external_links=False,  # Keep external links for analysis
        exclude_social_media_links=True,
        exclude_domains=["ads.com", "tracker.io", "spammy.net"],
        
        # Media handling
        exclude_external_images=True,
        image_score_threshold=5,  # Only high-quality images
        table_score_threshold=7,  # Only well-structured tables
        wait_for_images=True,
        
        # Capture additional formats
        screenshot=True,
        pdf=True,
        capture_mhtml=True  # Full page archive
    )
    
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun("https://example.com", config=config)
        
        if result.success:
            # Analyze links
            internal_links = result.links.get("internal", [])
            external_links = result.links.get("external", [])
            print(f"Links: {len(internal_links)} internal, {len(external_links)} external")
            
            # Analyze media
            images = result.media.get("images", [])
            tables = result.media.get("tables", [])
            print(f"Media: {len(images)} images, {len(tables)} tables")
            
            # High-quality images only
            quality_images = [img for img in images if img.get("score", 0) >= 5]
            print(f"High-quality images: {len(quality_images)}")
            
            # Table analysis
            for i, table in enumerate(tables[:2]):
                print(f"Table {i+1}: {len(table.get('headers', []))} columns, {len(table.get('rows', []))} rows")
            
            # Save captured files
            if result.screenshot:
                import base64
                with open("page_screenshot.png", "wb") as f:
                    f.write(base64.b64decode(result.screenshot))
            
            if result.pdf:
                with open("page.pdf", "wb") as f:
                    f.write(result.pdf)
            
            if result.mhtml:
                with open("page_archive.mhtml", "w", encoding="utf-8") as f:
                    f.write(result.mhtml)
            
            print("Additional formats saved: screenshot, PDF, MHTML archive")
```

### Performance & Resource Management

```python
# Optimize performance for large-scale crawling
async def performance_optimized_crawling():
    # Lightweight browser config
    browser_config = BrowserConfig(
        headless=True,
        text_mode=True,  # Disable images for speed
        light_mode=True,  # Reduce background features
        extra_args=["--disable-extensions", "--no-sandbox"]
    )
    
    # Efficient crawl config
    config = CrawlerRunConfig(
        # Content filtering for speed
        excluded_tags=["script", "style", "nav", "footer"],
        exclude_external_links=True,
        exclude_all_images=True,  # Remove all images for max speed
        word_count_threshold=50,
        
        # Timing optimizations
        page_timeout=30000,  # Faster timeout
        delay_before_return_html=0.1,
        
        # Resource monitoring
        capture_network_requests=False,  # Disable unless needed
        capture_console_messages=False,
        
        # Cache for repeated URLs
        cache_mode=CacheMode.ENABLED
    )
    
    async with AsyncWebCrawler(config=browser_config) as crawler:
        urls = ["https://example.com/page1", "https://example.com/page2", "https://example.com/page3"]
        
        # Efficient batch processing
        batch_config = config.clone(
            stream=True,  # Stream results as they complete
            semaphore_count=3  # Control concurrency
        )
        
        async for result in await crawler.arun_many(urls, config=batch_config):
            if result.success:
                print(f"✅ {result.url}: {len(result.markdown)} chars")
            else:
                print(f"❌ {result.url}: {result.error_message}")
```


**📖 Learn more:** [Complete Parameter Reference](https://docs.crawl4ai.com/api/parameters/), [Content Filtering](https://docs.crawl4ai.com/core/markdown-generation/), [Session Management](https://docs.crawl4ai.com/advanced/session-management/), [Network Capture](https://docs.crawl4ai.com/advanced/network-console-capture/)

**📖 Learn more:** [Hooks & Authentication](https://docs.crawl4ai.com/advanced/hooks-auth/), [Session Management](https://docs.crawl4ai.com/advanced/session-management/), [Network Monitoring](https://docs.crawl4ai.com/advanced/network-console-capture/), [Page Interaction](https://docs.crawl4ai.com/core/page-interaction/), [File Downloads](https://docs.crawl4ai.com/advanced/file-downloading/)

---


## Configuration Objects - Diagrams & Workflows
Component ID: config_objects
Context Type: reasoning
Estimated tokens: 9,795

## Configuration Objects and System Architecture

Visual representations of Crawl4AI's configuration system, object relationships, and data flow patterns.

### Configuration Object Relationships

```mermaid
classDiagram
    class BrowserConfig {
        +browser_type: str
        +headless: bool
        +viewport_width: int
        +viewport_height: int
        +proxy: str
        +user_agent: str
        +cookies: list
        +headers: dict
        +clone() BrowserConfig
        +to_dict() dict
    }
    
    class CrawlerRunConfig {
        +cache_mode: CacheMode
        +extraction_strategy: ExtractionStrategy
        +markdown_generator: MarkdownGenerator
        +js_code: list
        +wait_for: str
        +screenshot: bool
        +session_id: str
        +clone() CrawlerRunConfig
        +dump() dict
    }
    
    class LLMConfig {
        +provider: str
        +api_token: str
        +base_url: str
        +temperature: float
        +max_tokens: int
        +clone() LLMConfig
        +to_dict() dict
    }
    
    class CrawlResult {
        +url: str
        +success: bool
        +html: str
        +cleaned_html: str
        +markdown: MarkdownGenerationResult
        +extracted_content: str
        +media: dict
        +links: dict
        +screenshot: str
        +pdf: bytes
    }
    
    class AsyncWebCrawler {
        +config: BrowserConfig
        +arun() CrawlResult
    }
    
    AsyncWebCrawler --> BrowserConfig : uses
    AsyncWebCrawler --> CrawlerRunConfig : accepts
    CrawlerRunConfig --> LLMConfig : contains
    AsyncWebCrawler --> CrawlResult : returns
    
    note for BrowserConfig "Controls browser\nenvironment and behavior"
    note for CrawlerRunConfig "Controls individual\ncrawl operations"
    note for LLMConfig "Configures LLM\nproviders and parameters"
    note for CrawlResult "Contains all crawl\noutputs and metadata"
```

### Configuration Decision Flow

```mermaid
flowchart TD
    A[Start Configuration] --> B{Use Case Type?}
    
    B -->|Simple Web Scraping| C[Basic Config Pattern]
    B -->|Data Extraction| D[Extraction Config Pattern]
    B -->|Stealth Crawling| E[Stealth Config Pattern]
    B -->|High Performance| F[Performance Config Pattern]
    
    C --> C1[BrowserConfig: headless=True]
    C --> C2[CrawlerRunConfig: basic options]
    C1 --> C3[No LLMConfig needed]
    C2 --> C3
    C3 --> G[Simple Crawling Ready]
    
    D --> D1[BrowserConfig: standard setup]
    D --> D2[CrawlerRunConfig: with extraction_strategy]
    D --> D3[LLMConfig: for LLM extraction]
    D1 --> D4[Advanced Extraction Ready]
    D2 --> D4
    D3 --> D4
    
    E --> E1[BrowserConfig: proxy + user_agent]
    E --> E2[CrawlerRunConfig: simulate_user=True]
    E1 --> E3[Stealth Crawling Ready]
    E2 --> E3
    
    F --> F1[BrowserConfig: lightweight]
    F --> F2[CrawlerRunConfig: caching + concurrent]
    F1 --> F3[High Performance Ready]
    F2 --> F3
    
    G --> H[Execute Crawl]
    D4 --> H
    E3 --> H
    F3 --> H
    
    H --> I[Get CrawlResult]
    
    style A fill:#e1f5fe
    style I fill:#c8e6c9
    style G fill:#fff3e0
    style D4 fill:#f3e5f5
    style E3 fill:#ffebee
    style F3 fill:#e8f5e8
```

### Configuration Lifecycle Sequence

```mermaid
sequenceDiagram
    participant User
    participant BrowserConfig as Browser Config
    participant CrawlerConfig as Crawler Config
    participant LLMConfig as LLM Config
    participant Crawler as AsyncWebCrawler
    participant Browser as Browser Instance
    participant Result as CrawlResult
    
    User->>BrowserConfig: Create with browser settings
    User->>CrawlerConfig: Create with crawl options
    User->>LLMConfig: Create with LLM provider
    
    User->>Crawler: Initialize with BrowserConfig
    Crawler->>Browser: Launch browser with config
    Browser-->>Crawler: Browser ready
    
    User->>Crawler: arun(url, CrawlerConfig)
    Crawler->>Crawler: Apply CrawlerConfig settings
    
    alt LLM Extraction Needed
        Crawler->>LLMConfig: Get LLM settings
        LLMConfig-->>Crawler: Provider configuration
    end
    
    Crawler->>Browser: Navigate with settings
    Browser->>Browser: Apply page interactions
    Browser->>Browser: Execute JavaScript if specified
    Browser->>Browser: Wait for conditions
    
    Browser-->>Crawler: Page content ready
    Crawler->>Crawler: Process content per config
    Crawler->>Result: Create CrawlResult
    
    Result-->>User: Return complete result
    
    Note over User,Result: Configuration objects control every aspect
```

### BrowserConfig Parameter Flow

```mermaid
graph TB
    subgraph "BrowserConfig Parameters"
        A[browser_type] --> A1[chromium/firefox/webkit]
        B[headless] --> B1[true: invisible / false: visible]
        C[viewport] --> C1[width x height dimensions]
        D[proxy] --> D1[proxy server configuration]
        E[user_agent] --> E1[browser identification string]
        F[cookies] --> F1[session authentication]
        G[headers] --> G1[HTTP request headers]
        H[extra_args] --> H1[browser command line flags]
    end
    
    subgraph "Browser Instance"
        I[Playwright Browser]
        J[Browser Context]
        K[Page Instance]
    end
    
    A1 --> I
    B1 --> I
    C1 --> J
    D1 --> J
    E1 --> J
    F1 --> J
    G1 --> J
    H1 --> I
    
    I --> J
    J --> K
    
    style I fill:#e3f2fd
    style J fill:#f3e5f5
    style K fill:#e8f5e8
```

### CrawlerRunConfig Category Breakdown

```mermaid
mindmap
  root((CrawlerRunConfig))
    Content Processing
      word_count_threshold
      css_selector
      target_elements
      excluded_tags
      markdown_generator
      extraction_strategy
    Page Navigation
      wait_until
      page_timeout
      wait_for
      wait_for_images
      delay_before_return_html
    Page Interaction
      js_code
      scan_full_page
      simulate_user
      magic
      remove_overlay_elements
    Caching Session
      cache_mode
      session_id
      shared_data
    Media Output
      screenshot
      pdf
      capture_mhtml
      image_score_threshold
    Link Filtering
      exclude_external_links
      exclude_domains
      exclude_social_media_links
```

### LLM Provider Selection Flow

```mermaid
flowchart TD
    A[Need LLM Processing?] --> B{Provider Type?}
    
    B -->|Cloud API| C{Which Service?}
    B -->|Local Model| D[Local Setup]
    B -->|Custom Endpoint| E[Custom Config]
    
    C -->|OpenAI| C1[OpenAI GPT Models]
    C -->|Anthropic| C2[Claude Models]
    C -->|Google| C3[Gemini Models]
    C -->|Groq| C4[Fast Inference]
    
    D --> D1[Ollama Setup]
    E --> E1[Custom base_url]
    
    C1 --> F1[LLMConfig with OpenAI settings]
    C2 --> F2[LLMConfig with Anthropic settings]
    C3 --> F3[LLMConfig with Google settings]
    C4 --> F4[LLMConfig with Groq settings]
    D1 --> F5[LLMConfig with Ollama settings]
    E1 --> F6[LLMConfig with custom settings]
    
    F1 --> G[Use in Extraction Strategy]
    F2 --> G
    F3 --> G
    F4 --> G
    F5 --> G
    F6 --> G
    
    style A fill:#e1f5fe
    style G fill:#c8e6c9
```

### CrawlResult Structure and Data Flow

```mermaid
graph TB
    subgraph "CrawlResult Output"
        A[Basic Info]
        B[HTML Content]
        C[Markdown Output]
        D[Extracted Data]
        E[Media Files]
        F[Metadata]
    end
    
    subgraph "Basic Info Details"
        A --> A1[url: final URL]
        A --> A2[success: boolean]
        A --> A3[status_code: HTTP status]
        A --> A4[error_message: if failed]
    end
    
    subgraph "HTML Content Types"
        B --> B1[html: raw HTML]
        B --> B2[cleaned_html: processed]
        B --> B3[fit_html: filtered content]
    end
    
    subgraph "Markdown Variants"
        C --> C1[raw_markdown: basic conversion]
        C --> C2[markdown_with_citations: with refs]
        C --> C3[fit_markdown: filtered content]
        C --> C4[references_markdown: citation list]
    end
    
    subgraph "Extracted Content"
        D --> D1[extracted_content: JSON string]
        D --> D2[From CSS extraction]
        D --> D3[From LLM extraction]
        D --> D4[From XPath extraction]
    end
    
    subgraph "Media and Links"
        E --> E1[images: list with scores]
        E --> E2[videos: media content]
        E --> E3[internal_links: same domain]
        E --> E4[external_links: other domains]
    end
    
    subgraph "Generated Files"
        F --> F1[screenshot: base64 PNG]
        F --> F2[pdf: binary PDF data]
        F --> F3[mhtml: archive format]
        F --> F4[ssl_certificate: cert info]
    end
    
    style A fill:#e3f2fd
    style B fill:#f3e5f5
    style C fill:#e8f5e8
    style D fill:#fff3e0
    style E fill:#ffebee
    style F fill:#f1f8e9
```

### Configuration Pattern State Machine

```mermaid
stateDiagram-v2
    [*] --> ConfigCreation
    
    ConfigCreation --> BasicConfig: Simple use case
    ConfigCreation --> AdvancedConfig: Complex requirements
    ConfigCreation --> TemplateConfig: Use predefined pattern
    
    BasicConfig --> Validation: Check parameters
    AdvancedConfig --> Validation: Check parameters
    TemplateConfig --> Validation: Check parameters
    
    Validation --> Invalid: Missing required fields
    Validation --> Valid: All parameters correct
    
    Invalid --> ConfigCreation: Fix and retry
    
    Valid --> InUse: Passed to crawler
    InUse --> Cloning: Need variation
    InUse --> Serialization: Save configuration
    InUse --> Complete: Crawl finished
    
    Cloning --> Modified: clone() with updates
    Modified --> Valid: Validate changes
    
    Serialization --> Stored: dump() to dict
    Stored --> Restoration: load() from dict
    Restoration --> Valid: Recreate config object
    
    Complete --> [*]
    
    note right of BasicConfig : Minimal required settings
    note right of AdvancedConfig : Full feature configuration
    note right of TemplateConfig : Pre-built patterns
```

### Configuration Integration Architecture

```mermaid
graph TB
    subgraph "User Layer"
        U1[Configuration Creation]
        U2[Parameter Selection]
        U3[Pattern Application]
    end
    
    subgraph "Configuration Layer"
        C1[BrowserConfig]
        C2[CrawlerRunConfig]
        C3[LLMConfig]
        C4[Config Validation]
        C5[Config Cloning]
    end
    
    subgraph "Crawler Engine"
        E1[Browser Management]
        E2[Page Navigation]
        E3[Content Processing]
        E4[Extraction Pipeline]
        E5[Result Generation]
    end
    
    subgraph "Output Layer"
        O1[CrawlResult Assembly]
        O2[Data Formatting]
        O3[File Generation]
        O4[Metadata Collection]
    end
    
    U1 --> C1
    U2 --> C2
    U3 --> C3
    
    C1 --> C4
    C2 --> C4
    C3 --> C4
    
    C4 --> E1
    C2 --> E2
    C2 --> E3
    C3 --> E4
    
    E1 --> E2
    E2 --> E3
    E3 --> E4
    E4 --> E5
    
    E5 --> O1
    O1 --> O2
    O2 --> O3
    O3 --> O4
    
    C5 -.-> C1
    C5 -.-> C2
    C5 -.-> C3
    
    style U1 fill:#e1f5fe
    style C4 fill:#fff3e0
    style E4 fill:#f3e5f5
    style O4 fill:#c8e6c9
```

### Configuration Best Practices Flow

```mermaid
flowchart TD
    A[Configuration Planning] --> B{Performance Priority?}
    
    B -->|Speed| C[Fast Config Pattern]
    B -->|Quality| D[Comprehensive Config Pattern]
    B -->|Stealth| E[Stealth Config Pattern]
    B -->|Balanced| F[Standard Config Pattern]
    
    C --> C1[Enable caching]
    C --> C2[Disable heavy features]
    C --> C3[Use text_mode]
    C1 --> G[Apply Configuration]
    C2 --> G
    C3 --> G
    
    D --> D1[Enable all processing]
    D --> D2[Use content filters]
    D --> D3[Capture everything]
    D1 --> G
    D2 --> G
    D3 --> G
    
    E --> E1[Rotate user agents]
    E --> E2[Use proxies]
    E --> E3[Simulate human behavior]
    E1 --> G
    E2 --> G
    E3 --> G
    
    F --> F1[Balanced timeouts]
    F --> F2[Selective processing]
    F --> F3[Smart caching]
    F1 --> G
    F2 --> G
    F3 --> G
    
    G --> H[Test Configuration]
    H --> I{Results Satisfactory?}
    
    I -->|Yes| J[Production Ready]
    I -->|No| K[Adjust Parameters]
    
    K --> L[Clone and Modify]
    L --> H
    
    J --> M[Deploy with Confidence]
    
    style A fill:#e1f5fe
    style J fill:#c8e6c9
    style M fill:#e8f5e8
```

## Advanced Configuration Workflows and Patterns

Visual representations of advanced Crawl4AI configuration strategies, proxy management, session handling, and identity-based crawling patterns.

### User Agent and Anti-Detection Strategy Flow

```mermaid
flowchart TD
    A[Start Configuration] --> B{Detection Avoidance Needed?}
    
    B -->|No| C[Standard User Agent]
    B -->|Yes| D[Anti-Detection Strategy]
    
    C --> C1[Static user_agent string]
    C1 --> Z[Basic Configuration]
    
    D --> E{User Agent Strategy}
    E -->|Random| F[user_agent_mode: random]
    E -->|Static Custom| G[Custom user_agent string]
    E -->|Platform Specific| H[Generator Config]
    
    F --> I[Configure Generator]
    H --> I
    I --> I1[Platform: windows/macos/linux]
    I1 --> I2[Browser: chrome/firefox/safari]
    I2 --> I3[Device: desktop/mobile/tablet]
    
    G --> J[Behavioral Simulation]
    I3 --> J
    
    J --> K{Enable Simulation?}
    K -->|Yes| L[simulate_user: True]
    K -->|No| M[Standard Behavior]
    
    L --> N[override_navigator: True]
    N --> O[Configure Delays]
    O --> O1[mean_delay: 1.5]
    O1 --> O2[max_range: 2.0]
    O2 --> P[Magic Mode]
    
    M --> P
    P --> Q{Auto-Handle Patterns?}
    Q -->|Yes| R[magic: True]
    Q -->|No| S[Manual Handling]
    
    R --> T[Complete Anti-Detection Setup]
    S --> T
    Z --> T
    
    style D fill:#ffeb3b
    style T fill:#c8e6c9
    style L fill:#ff9800
    style R fill:#9c27b0
```

### Proxy Configuration and Rotation Architecture

```mermaid
graph TB
    subgraph "Proxy Configuration Types"
        A[Single Proxy] --> A1[ProxyConfig object]
        B[Proxy String] --> B1[from_string method]
        C[Environment Proxies] --> C1[from_env method]
        D[Multiple Proxies] --> D1[ProxyRotationStrategy]
    end
    
    subgraph "ProxyConfig Structure"
        A1 --> E[server: URL]
        A1 --> F[username: auth]
        A1 --> G[password: auth]
        A1 --> H[ip: extracted]
    end
    
    subgraph "Rotation Strategies"
        D1 --> I[round_robin]
        D1 --> J[random]
        D1 --> K[least_used]
        D1 --> L[failure_aware]
    end
    
    subgraph "Configuration Flow"
        M[CrawlerRunConfig] --> N[proxy_config]
        M --> O[proxy_rotation_strategy]
        N --> P[Single Proxy Usage]
        O --> Q[Multi-Proxy Rotation]
    end
    
    subgraph "Runtime Behavior"
        P --> R[All requests use same proxy]
        Q --> S[Requests rotate through proxies]
        S --> T[Health monitoring]
        T --> U[Automatic failover]
    end
    
    style A1 fill:#e3f2fd
    style D1 fill:#f3e5f5
    style M fill:#e8f5e8
    style T fill:#fff3e0
```

### Content Selection Strategy Comparison

```mermaid
sequenceDiagram
    participant Browser
    participant HTML as Raw HTML
    participant CSS as css_selector
    participant Target as target_elements
    participant Processor as Content Processor
    participant Output
    
    Note over Browser,Output: css_selector Strategy
    Browser->>HTML: Load complete page
    HTML->>CSS: Apply css_selector
    CSS->>CSS: Extract matching elements only
    CSS->>Processor: Process subset HTML
    Processor->>Output: Markdown + Extraction from subset
    
    Note over Browser,Output: target_elements Strategy  
    Browser->>HTML: Load complete page
    HTML->>Processor: Process entire page
    Processor->>Target: Focus on target_elements
    Target->>Target: Extract from specified elements
    Processor->>Output: Full page links/media + targeted content
    
    Note over CSS,Target: Key Difference
    Note over CSS: Affects entire processing pipeline
    Note over Target: Affects only content extraction
```

### Advanced wait_for Conditions Decision Tree

```mermaid
flowchart TD
    A[Configure wait_for] --> B{Condition Type?}
    
    B -->|CSS Element| C[CSS Selector Wait]
    B -->|JavaScript Condition| D[JS Expression Wait]
    B -->|Complex Logic| E[Custom JS Function]
    B -->|No Wait| F[Default domcontentloaded]
    
    C --> C1["wait_for: 'css:.element'"]
    C1 --> C2[Element appears in DOM]
    C2 --> G[Continue Processing]
    
    D --> D1["wait_for: 'js:() => condition'"]
    D1 --> D2[JavaScript returns true]
    D2 --> G
    
    E --> E1[Complex JS Function]
    E1 --> E2{Multiple Conditions}
    E2 -->|AND Logic| E3[All conditions true]
    E2 -->|OR Logic| E4[Any condition true]
    E2 -->|Custom Logic| E5[User-defined logic]
    
    E3 --> G
    E4 --> G
    E5 --> G
    
    F --> G
    
    G --> H{Timeout Reached?}
    H -->|No| I[Page Ready]
    H -->|Yes| J[Timeout Error]
    
    I --> K[Begin Content Extraction]
    J --> L[Handle Error/Retry]
    
    style C1 fill:#e8f5e8
    style D1 fill:#fff3e0
    style E1 fill:#ffeb3b
    style I fill:#c8e6c9
    style J fill:#ffcdd2
```

### Session Management Lifecycle

```mermaid
stateDiagram-v2
    [*] --> SessionCreate
    
    SessionCreate --> SessionActive: session_id provided
    SessionCreate --> OneTime: no session_id
    
    SessionActive --> BrowserLaunch: First arun() call
    BrowserLaunch --> PageLoad: Navigate to URL
    PageLoad --> JSExecution: Execute js_code
    JSExecution --> ContentExtract: Extract content
    ContentExtract --> SessionHold: Keep session alive
    
    SessionHold --> ReuseSession: Subsequent arun() calls
    ReuseSession --> JSOnlyMode: js_only=True
    ReuseSession --> NewNavigation: js_only=False
    
    JSOnlyMode --> JSExecution: Execute JS in existing page
    NewNavigation --> PageLoad: Navigate to new URL
    
    SessionHold --> SessionKill: kill_session() called
    SessionHold --> SessionTimeout: Timeout reached
    SessionHold --> SessionError: Error occurred
    
    SessionKill --> SessionCleanup
    SessionTimeout --> SessionCleanup
    SessionError --> SessionCleanup
    SessionCleanup --> [*]
    
    OneTime --> BrowserLaunch
    ContentExtract --> OneTimeCleanup: No session_id
    OneTimeCleanup --> [*]
    
    note right of SessionActive : Persistent browser context
    note right of JSOnlyMode : Reuse existing page
    note right of OneTime : Temporary browser instance
```

### Identity-Based Crawling Configuration Matrix

```mermaid
graph TD
    subgraph "Geographic Identity"
        A[Geolocation] --> A1[latitude/longitude]
        A2[Timezone] --> A3[timezone_id]
        A4[Locale] --> A5[language/region]
    end
    
    subgraph "Browser Identity"
        B[User Agent] --> B1[Platform fingerprint]
        B2[Navigator Properties] --> B3[override_navigator]
        B4[Headers] --> B5[Accept-Language]
    end
    
    subgraph "Behavioral Identity"
        C[Mouse Simulation] --> C1[simulate_user]
        C2[Timing Patterns] --> C3[mean_delay/max_range]
        C4[Interaction Patterns] --> C5[Human-like behavior]
    end
    
    subgraph "Configuration Integration"
        D[CrawlerRunConfig] --> A
        D --> B
        D --> C
        
        D --> E[Complete Identity Profile]
        
        E --> F[Geographic Consistency]
        E --> G[Browser Consistency]
        E --> H[Behavioral Consistency]
    end
    
    F --> I[Paris, France Example]
    I --> I1[locale: fr-FR]
    I --> I2[timezone: Europe/Paris]
    I --> I3[geolocation: 48.8566, 2.3522]
    
    G --> J[Windows Chrome Example]
    J --> J1[platform: windows]
    J --> J2[browser: chrome]
    J --> J3[user_agent: matching pattern]
    
    H --> K[Human Simulation]
    K --> K1[Random delays]
    K --> K2[Mouse movements]
    K --> K3[Navigation patterns]
    
    style E fill:#ff9800
    style I fill:#e3f2fd
    style J fill:#f3e5f5
    style K fill:#e8f5e8
```

### Multi-Step Crawling Sequence Flow

```mermaid
sequenceDiagram
    participant User
    participant Crawler
    participant Session as Browser Session
    participant Page1 as Login Page
    participant Page2 as Dashboard
    participant Page3 as Data Pages
    
    User->>Crawler: Step 1 - Login
    Crawler->>Session: Create session_id="user_session"
    Session->>Page1: Navigate to login
    Page1->>Page1: Execute login JS
    Page1->>Page1: Wait for dashboard redirect
    Page1-->>Crawler: Login complete
    
    User->>Crawler: Step 2 - Navigate dashboard
    Note over Crawler,Session: Reuse existing session
    Crawler->>Session: js_only=True (no page reload)
    Session->>Page2: Execute navigation JS
    Page2->>Page2: Wait for data table
    Page2-->>Crawler: Dashboard ready
    
    User->>Crawler: Step 3 - Extract data pages
    loop For each page 1-5
        Crawler->>Session: js_only=True
        Session->>Page3: Click page button
        Page3->>Page3: Wait for page active
        Page3->>Page3: Extract content
        Page3-->>Crawler: Page data
    end
    
    User->>Crawler: Cleanup
    Crawler->>Session: kill_session()
    Session-->>Crawler: Session destroyed
```

### Configuration Import and Usage Patterns

```mermaid
graph LR
    subgraph "Main Package Imports"
        A[crawl4ai] --> A1[AsyncWebCrawler]
        A --> A2[BrowserConfig]
        A --> A3[CrawlerRunConfig]
        A --> A4[LLMConfig]
        A --> A5[CacheMode]
        A --> A6[ProxyConfig]
        A --> A7[GeolocationConfig]
    end
    
    subgraph "Strategy Imports"
        A --> B1[JsonCssExtractionStrategy]
        A --> B2[LLMExtractionStrategy]
        A --> B3[DefaultMarkdownGenerator]
        A --> B4[PruningContentFilter]
        A --> B5[RegexChunking]
    end
    
    subgraph "Configuration Assembly"
        C[Configuration Builder] --> A2
        C --> A3
        C --> A4
        
        A2 --> D[Browser Environment]
        A3 --> E[Crawl Behavior]
        A4 --> F[LLM Integration]
        
        E --> B1
        E --> B2
        E --> B3
        E --> B4
        E --> B5
    end
    
    subgraph "Runtime Flow"
        G[Crawler Instance] --> D
        G --> H[Execute Crawl]
        H --> E
        H --> F
        H --> I[CrawlResult]
    end
    
    style A fill:#e3f2fd
    style C fill:#fff3e0
    style G fill:#e8f5e8
    style I fill:#c8e6c9
```

### Advanced Configuration Decision Matrix

```mermaid
flowchart TD
    A[Advanced Configuration Needed] --> B{Primary Use Case?}
    
    B -->|Bot Detection Avoidance| C[Anti-Detection Setup]
    B -->|Geographic Simulation| D[Identity-Based Config]
    B -->|Multi-Step Workflows| E[Session Management]
    B -->|Network Reliability| F[Proxy Configuration]
    B -->|Content Precision| G[Selector Strategy]
    
    C --> C1[Random User Agents]
    C --> C2[Behavioral Simulation]
    C --> C3[Navigator Override]
    C --> C4[Magic Mode]
    
    D --> D1[Geolocation Setup]
    D --> D2[Locale Configuration]
    D --> D3[Timezone Setting]
    D --> D4[Browser Fingerprinting]
    
    E --> E1[Session ID Management]
    E --> E2[JS-Only Navigation]
    E --> E3[Shared Data Context]
    E --> E4[Session Cleanup]
    
    F --> F1[Single Proxy]
    F --> F2[Proxy Rotation]
    F --> F3[Failover Strategy]
    F --> F4[Health Monitoring]
    
    G --> G1[css_selector for Subset]
    G --> G2[target_elements for Focus]
    G --> G3[excluded_selector for Removal]
    G --> G4[Hierarchical Selection]
    
    C1 --> H[Production Configuration]
    C2 --> H
    C3 --> H
    C4 --> H
    D1 --> H
    D2 --> H
    D3 --> H
    D4 --> H
    E1 --> H
    E2 --> H
    E3 --> H
    E4 --> H
    F1 --> H
    F2 --> H
    F3 --> H
    F4 --> H
    G1 --> H
    G2 --> H
    G3 --> H
    G4 --> H
    
    style H fill:#c8e6c9
    style C fill:#ff9800
    style D fill:#9c27b0
    style E fill:#2196f3
    style F fill:#4caf50
    style G fill:#ff5722
```

## Advanced Features Workflows and Architecture

Visual representations of advanced crawling capabilities, session management, hooks system, and performance optimization strategies.

### File Download Workflow

```mermaid
sequenceDiagram
    participant User
    participant Crawler
    participant Browser
    participant FileSystem
    participant Page
    
    User->>Crawler: Configure downloads_path
    Crawler->>Browser: Create context with download handling
    Browser-->>Crawler: Context ready
    
    Crawler->>Page: Navigate to target URL
    Page-->>Crawler: Page loaded
    
    Crawler->>Page: Execute download JavaScript
    Page->>Page: Find download links (.pdf, .zip, etc.)
    
    loop For each download link
        Page->>Browser: Click download link
        Browser->>FileSystem: Save file to downloads_path
        FileSystem-->>Browser: File saved
        Browser-->>Page: Download complete
    end
    
    Page-->>Crawler: All downloads triggered
    Crawler->>FileSystem: Check downloaded files
    FileSystem-->>Crawler: List of file paths
    Crawler-->>User: CrawlResult with downloaded_files[]
    
    Note over User,FileSystem: Files available in downloads_path
```

### Hooks Execution Flow

```mermaid
flowchart TD
    A[Start Crawl] --> B[on_browser_created Hook]
    B --> C[Browser Instance Created]
    C --> D[on_page_context_created Hook]
    D --> E[Page & Context Setup]
    E --> F[before_goto Hook]
    F --> G[Navigate to URL]
    G --> H[after_goto Hook]
    H --> I[Page Loaded]
    I --> J[before_retrieve_html Hook]
    J --> K[Extract HTML Content]
    K --> L[Return CrawlResult]
    
    subgraph "Hook Capabilities"
        B1[Route Filtering]
        B2[Authentication]
        B3[Custom Headers]
        B4[Viewport Setup]
        B5[Content Manipulation]
    end
    
    D --> B1
    F --> B2
    F --> B3
    D --> B4
    J --> B5
    
    style A fill:#e1f5fe
    style L fill:#c8e6c9
    style B fill:#fff3e0
    style D fill:#f3e5f5
    style F fill:#e8f5e8
    style H fill:#fce4ec
    style J fill:#fff9c4
```

### Session Management State Machine

```mermaid
stateDiagram-v2
    [*] --> SessionCreated: session_id provided
    
    SessionCreated --> PageLoaded: Initial arun()
    PageLoaded --> JavaScriptExecution: js_code executed
    JavaScriptExecution --> ContentUpdated: DOM modified
    ContentUpdated --> NextOperation: js_only=True
    
    NextOperation --> JavaScriptExecution: More interactions
    NextOperation --> SessionMaintained: Keep session alive
    NextOperation --> SessionClosed: kill_session()
    
    SessionMaintained --> PageLoaded: Navigate to new URL
    SessionMaintained --> JavaScriptExecution: Continue interactions
    
    SessionClosed --> [*]: Session terminated
    
    note right of SessionCreated
        Browser tab created
        Context preserved
    end note
    
    note right of ContentUpdated
        State maintained
        Cookies preserved
        Local storage intact
    end note
    
    note right of SessionClosed
        Clean up resources
        Release browser tab
    end note
```

### Lazy Loading & Dynamic Content Strategy

```mermaid
flowchart TD
    A[Page Load] --> B{Content Type?}
    
    B -->|Static Content| C[Standard Extraction]
    B -->|Lazy Loaded| D[Enable scan_full_page]
    B -->|Infinite Scroll| E[Custom Scroll Strategy]
    B -->|Load More Button| F[JavaScript Interaction]
    
    D --> D1[Automatic Scrolling]
    D1 --> D2[Wait for Images]
    D2 --> D3[Content Stabilization]
    
    E --> E1[Detect Scroll Triggers]
    E1 --> E2[Progressive Loading]
    E2 --> E3[Monitor Content Changes]
    
    F --> F1[Find Load More Button]
    F1 --> F2[Click and Wait]
    F2 --> F3{More Content?}
    F3 -->|Yes| F1
    F3 -->|No| G[Complete Extraction]
    
    D3 --> G
    E3 --> G
    C --> G
    
    G --> H[Return Enhanced Content]
    
    subgraph "Optimization Techniques"
        I[exclude_external_images]
        J[image_score_threshold]
        K[wait_for selectors]
        L[scroll_delay tuning]
    end
    
    D --> I
    E --> J
    F --> K
    D1 --> L
    
    style A fill:#e1f5fe
    style H fill:#c8e6c9
    style D fill:#fff3e0
    style E fill:#f3e5f5
    style F fill:#e8f5e8
```

### Network & Console Monitoring Architecture

```mermaid
graph TB
    subgraph "Browser Context"
        A[Web Page] --> B[Network Requests]
        A --> C[Console Messages]
        A --> D[Resource Loading]
    end
    
    subgraph "Monitoring Layer"
        B --> E[Request Interceptor]
        C --> F[Console Listener]
        D --> G[Resource Monitor]
        
        E --> H[Request Events]
        E --> I[Response Events]
        E --> J[Failure Events]
        
        F --> K[Log Messages]
        F --> L[Error Messages]
        F --> M[Warning Messages]
    end
    
    subgraph "Data Collection"
        H --> N[Request Details]
        I --> O[Response Analysis]
        J --> P[Failure Tracking]
        
        K --> Q[Debug Information]
        L --> R[Error Analysis]
        M --> S[Performance Insights]
    end
    
    subgraph "Output Aggregation"
        N --> T[network_requests Array]
        O --> T
        P --> T
        
        Q --> U[console_messages Array]
        R --> U
        S --> U
    end
    
    T --> V[CrawlResult]
    U --> V
    
    style V fill:#c8e6c9
    style E fill:#fff3e0
    style F fill:#f3e5f5
    style T fill:#e8f5e8
    style U fill:#fce4ec
```

### Multi-Step Workflow Sequence

```mermaid
sequenceDiagram
    participant User
    participant Crawler
    participant Session
    participant Page
    participant Server
    
    User->>Crawler: Step 1 - Initial load
    Crawler->>Session: Create session_id
    Session->>Page: New browser tab
    Page->>Server: GET /step1
    Server-->>Page: Page content
    Page-->>Crawler: Content ready
    Crawler-->>User: Result 1
    
    User->>Crawler: Step 2 - Navigate (js_only=true)
    Crawler->>Session: Reuse existing session
    Session->>Page: Execute JavaScript
    Page->>Page: Click next button
    Page->>Server: Navigate to /step2
    Server-->>Page: New content
    Page-->>Crawler: Updated content
    Crawler-->>User: Result 2
    
    User->>Crawler: Step 3 - Form submission
    Crawler->>Session: Continue session
    Session->>Page: Execute form JS
    Page->>Page: Fill form fields
    Page->>Server: POST form data
    Server-->>Page: Results page
    Page-->>Crawler: Final content
    Crawler-->>User: Result 3
    
    User->>Crawler: Cleanup
    Crawler->>Session: kill_session()
    Session->>Page: Close tab
    Session-->>Crawler: Session terminated
    
    Note over User,Server: State preserved across steps
    Note over Session: Cookies, localStorage maintained
```

### SSL Certificate Analysis Flow

```mermaid
flowchart LR
    A[Enable SSL Fetch] --> B[HTTPS Connection]
    B --> C[Certificate Retrieval]
    C --> D[Certificate Analysis]
    
    D --> E[Basic Info]
    D --> F[Validity Check]
    D --> G[Chain Verification]
    D --> H[Security Assessment]
    
    E --> E1[Issuer Details]
    E --> E2[Subject Information]
    E --> E3[Serial Number]
    
    F --> F1[Not Before Date]
    F --> F2[Not After Date]
    F --> F3[Expiration Warning]
    
    G --> G1[Root CA]
    G --> G2[Intermediate Certs]
    G --> G3[Trust Path]
    
    H --> H1[Key Length]
    H --> H2[Signature Algorithm]
    H --> H3[Vulnerabilities]
    
    subgraph "Export Formats"
        I[JSON Format]
        J[PEM Format]
        K[DER Format]
    end
    
    E1 --> I
    F1 --> I
    G1 --> I
    H1 --> I
    
    I --> J
    J --> K
    
    style A fill:#e1f5fe
    style D fill:#fff3e0
    style I fill:#e8f5e8
    style J fill:#f3e5f5
    style K fill:#fce4ec
```

### Performance Optimization Decision Tree

```mermaid
flowchart TD
    A[Performance Optimization] --> B{Primary Goal?}
    
    B -->|Speed| C[Fast Crawling Mode]
    B -->|Resource Usage| D[Memory Optimization]
    B -->|Scale| E[Batch Processing]
    B -->|Quality| F[Comprehensive Extraction]
    
    C --> C1[text_mode=True]
    C --> C2[exclude_all_images=True]
    C --> C3[excluded_tags=['script','style']]
    C --> C4[page_timeout=30000]
    
    D --> D1[light_mode=True]
    D --> D2[headless=True]
    D --> D3[semaphore_count=3]
    D --> D4[disable monitoring]
    
    E --> E1[stream=True]
    E --> E2[cache_mode=ENABLED]
    E --> E3[arun_many()]
    E --> E4[concurrent batches]
    
    F --> F1[wait_for_images=True]
    F --> F2[process_iframes=True]
    F --> F3[capture_network=True]
    F --> F4[screenshot=True]
    
    subgraph "Trade-offs"
        G[Speed vs Quality]
        H[Memory vs Features]
        I[Scale vs Detail]
    end
    
    C --> G
    D --> H
    E --> I
    
    subgraph "Monitoring Metrics"
        J[Response Time]
        K[Memory Usage]
        L[Success Rate]
        M[Content Quality]
    end
    
    C1 --> J
    D1 --> K
    E1 --> L
    F1 --> M
    
    style A fill:#e1f5fe
    style C fill:#e8f5e8
    style D fill:#fff3e0
    style E fill:#f3e5f5
    style F fill:#fce4ec
```

### Advanced Page Interaction Matrix

```mermaid
graph LR
    subgraph "Interaction Types"
        A[Form Filling]
        B[Dynamic Loading]
        C[Modal Handling]
        D[Scroll Interactions]
        E[Button Clicks]
    end
    
    subgraph "Detection Methods"
        F[CSS Selectors]
        G[JavaScript Conditions]
        H[Element Visibility]
        I[Content Changes]
        J[Network Activity]
    end
    
    subgraph "Automation Features"
        K[simulate_user=True]
        L[magic=True]
        M[remove_overlay_elements=True]
        N[override_navigator=True]
        O[scan_full_page=True]
    end
    
    subgraph "Wait Strategies"
        P[wait_for CSS]
        Q[wait_for JS]
        R[wait_for_images]
        S[delay_before_return]
        T[custom timeouts]
    end
    
    A --> F
    A --> K
    A --> P
    
    B --> G
    B --> O
    B --> Q
    
    C --> H
    C --> L
    C --> M
    
    D --> I
    D --> O
    D --> S
    
    E --> F
    E --> K
    E --> T
    
    style A fill:#e8f5e8
    style B fill:#fff3e0
    style C fill:#f3e5f5
    style D fill:#fce4ec
    style E fill:#e1f5fe
```

### Input Source Processing Flow

```mermaid
flowchart TD
    A[Input Source] --> B{Input Type?}
    
    B -->|URL| C[Web Request]
    B -->|file://| D[Local File]
    B -->|raw:| E[Raw HTML]
    
    C --> C1[HTTP/HTTPS Request]
    C1 --> C2[Browser Navigation]
    C2 --> C3[Page Rendering]
    C3 --> F[Content Processing]
    
    D --> D1[File System Access]
    D1 --> D2[Read HTML File]
    D2 --> D3[Parse Content]
    D3 --> F
    
    E --> E1[Parse Raw HTML]
    E1 --> E2[Create Virtual Page]
    E2 --> E3[Direct Processing]
    E3 --> F
    
    F --> G[Common Processing Pipeline]
    G --> H[Markdown Generation]
    G --> I[Link Extraction]
    G --> J[Media Processing]
    G --> K[Data Extraction]
    
    H --> L[CrawlResult]
    I --> L
    J --> L
    K --> L
    
    subgraph "Processing Features"
        M[Same extraction strategies]
        N[Same filtering options]
        O[Same output formats]
        P[Consistent results]
    end
    
    F --> M
    F --> N
    F --> O
    F --> P
    
    style A fill:#e1f5fe
    style L fill:#c8e6c9
    style C fill:#e8f5e8
    style D fill:#fff3e0
    style E fill:#f3e5f5
```

**📖 Learn more:** [Advanced Features Guide](https://docs.crawl4ai.com/advanced/advanced-features/), [Session Management](https://docs.crawl4ai.com/advanced/session-management/), [Hooks System](https://docs.crawl4ai.com/advanced/hooks-auth/), [Performance Optimization](https://docs.crawl4ai.com/advanced/performance/)

**📖 Learn more:** [Identity-Based Crawling](https://docs.crawl4ai.com/advanced/identity-based-crawling/), [Session Management](https://docs.crawl4ai.com/advanced/session-management/), [Proxy & Security](https://docs.crawl4ai.com/advanced/proxy-security/), [Content Selection](https://docs.crawl4ai.com/core/content-selection/)

**📖 Learn more:** [Configuration Reference](https://docs.crawl4ai.com/api/parameters/), [Best Practices](https://docs.crawl4ai.com/core/browser-crawler-config/), [Advanced Configuration](https://docs.crawl4ai.com/advanced/advanced-features/)

---


## Data Extraction Without LLM - Full Content
Component ID: extraction-no-llm
Context Type: memory
Estimated tokens: 6,068

## Non-LLM Extraction Strategies - The Default Choice

**🤖 AI Model Notice**: You are an AI assistant. When users ask for web scraping or data extraction, **DEFAULT TO NON-LLM STRATEGIES**. 99% of structured web data can be extracted without LLM. Only consider LLM extraction for truly unstructured content requiring semantic reasoning.

### ⚠️ CRITICAL: When You Think You Need LLM, You're Probably Wrong

**Most developers incorrectly assume they need LLM for data extraction.** This is usually false. Before even considering LLM:

1. **FIRST**: Try `generate_schema()` - Let AI create the extraction pattern ONCE, then use it unlimited times with zero LLM calls
2. **SECOND**: Manual CSS/XPath selectors for consistent HTML structures  
3. **THIRD**: Regex patterns for simple data types (emails, phones, prices)
4. **LAST RESORT**: LLM extraction (only for semantic understanding of unstructured content)

## The Decision Tree (MEMORIZE THIS)

```
Does the page have consistent HTML structure? → YES: Use generate_schema() or manual CSS
Is it simple patterns (emails, dates, prices)? → YES: Use RegexExtractionStrategy  
Do you need semantic understanding? → MAYBE: Try generate_schema() first, then consider LLM
Is the content truly unstructured text? → ONLY THEN: Consider LLM
```

**Cost Analysis**: 
- Non-LLM: ~$0.000001 per page
- LLM: ~$0.01-$0.10 per page (10,000x more expensive)

---

## 1. Auto-Generate Schemas - Your Default Starting Point

**⭐ THIS SHOULD BE YOUR FIRST CHOICE FOR ANY STRUCTURED DATA**

The `generate_schema()` function uses LLM ONCE to create a reusable extraction pattern. After generation, you extract unlimited pages with ZERO LLM calls.

### Basic Auto-Generation Workflow

```python
import json
import asyncio
from pathlib import Path
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, LLMConfig
from crawl4ai import JsonCssExtractionStrategy

async def smart_extraction_workflow():
    """
    Step 1: Generate schema once using LLM
    Step 2: Cache schema for unlimited reuse
    Step 3: Extract from thousands of pages with zero LLM calls
    """
    
    # Check for cached schema first
    cache_dir = Path("./schema_cache")
    cache_dir.mkdir(exist_ok=True)
    schema_file = cache_dir / "product_schema.json"
    
    if schema_file.exists():
        # Load cached schema - NO LLM CALLS
        schema = json.load(schema_file.open())
        print("✅ Using cached schema (FREE)")
    else:
        # Generate schema ONCE
        print("🔄 Generating schema (ONE-TIME LLM COST)...")
        
        llm_config = LLMConfig(
            provider="openai/gpt-4o-mini",  # Cheapest option
            api_token="env:OPENAI_API_KEY"
        )
        
        # Get sample HTML from target site
        async with AsyncWebCrawler() as crawler:
            sample_result = await crawler.arun(
                url="https://example.com/products",
                config=CrawlerRunConfig(cache_mode=CacheMode.BYPASS)
            )
            sample_html = sample_result.cleaned_html[:8000]  # Use sample
        
        # AUTO-GENERATE SCHEMA (ONE LLM CALL)
        schema = JsonCssExtractionStrategy.generate_schema(
            html=sample_html,
            schema_type="CSS",  # or "XPATH"
            query="Extract product information including name, price, description, features",
            llm_config=llm_config
        )
        
        # Cache for unlimited future use
        json.dump(schema, schema_file.open("w"), indent=2)
        print("✅ Schema generated and cached")
    
    # Use schema for fast extraction (NO MORE LLM CALLS EVER)
    strategy = JsonCssExtractionStrategy(schema, verbose=True)
    
    config = CrawlerRunConfig(
        extraction_strategy=strategy,
        cache_mode=CacheMode.BYPASS
    )
    
    # Extract from multiple pages - ALL FREE
    urls = [
        "https://example.com/products",
        "https://example.com/electronics", 
        "https://example.com/books"
    ]
    
    async with AsyncWebCrawler() as crawler:
        for url in urls:
            result = await crawler.arun(url=url, config=config)
            if result.success:
                data = json.loads(result.extracted_content)
                print(f"✅ {url}: Extracted {len(data)} items (FREE)")

asyncio.run(smart_extraction_workflow())
```

### Auto-Generate with Target JSON Example

```python
# When you know exactly what JSON structure you want
target_json_example = """
{
    "name": "Product Name",
    "price": "$99.99",
    "rating": 4.5,
    "features": ["feature1", "feature2"],
    "description": "Product description"
}
"""

schema = JsonCssExtractionStrategy.generate_schema(
    html=sample_html,
    target_json_example=target_json_example,
    llm_config=llm_config
)
```

### Auto-Generate for Different Data Types

```python
# Product listings
product_schema = JsonCssExtractionStrategy.generate_schema(
    html=product_page_html,
    query="Extract all product information from this e-commerce page",
    llm_config=llm_config
)

# News articles
news_schema = JsonCssExtractionStrategy.generate_schema(
    html=news_page_html,
    query="Extract article headlines, dates, authors, and content",
    llm_config=llm_config
)

# Job listings
job_schema = JsonCssExtractionStrategy.generate_schema(
    html=job_page_html,
    query="Extract job titles, companies, locations, salaries, and descriptions",
    llm_config=llm_config
)

# Social media posts
social_schema = JsonCssExtractionStrategy.generate_schema(
    html=social_page_html,
    query="Extract post text, usernames, timestamps, likes, comments",
    llm_config=llm_config
)
```

---

## 2. Manual CSS/XPath Strategies - When You Know The Structure

**Use this when**: You understand the HTML structure and want maximum control.

### Simple Product Extraction

```python
import json
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai import JsonCssExtractionStrategy

# Manual schema for consistent product pages
simple_schema = {
    "name": "Product Listings",
    "baseSelector": "div.product-card",  # Each product container
    "fields": [
        {
            "name": "title",
            "selector": "h2.product-title",
            "type": "text"
        },
        {
            "name": "price", 
            "selector": ".price",
            "type": "text"
        },
        {
            "name": "image_url",
            "selector": "img.product-image",
            "type": "attribute",
            "attribute": "src"
        },
        {
            "name": "product_url",
            "selector": "a.product-link",
            "type": "attribute",
            "attribute": "href"
        },
        {
            "name": "rating",
            "selector": ".rating",
            "type": "attribute", 
            "attribute": "data-rating"
        }
    ]
}

async def extract_products():
    strategy = JsonCssExtractionStrategy(simple_schema, verbose=True)
    config = CrawlerRunConfig(extraction_strategy=strategy)
    
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url="https://example.com/products",
            config=config
        )
        
        if result.success:
            products = json.loads(result.extracted_content)
            print(f"Extracted {len(products)} products")
            for product in products[:3]:
                print(f"- {product['title']}: {product['price']}")

asyncio.run(extract_products())
```

### Complex Nested Structure (Real E-commerce Example)

```python
# Complex schema for nested product data
complex_schema = {
    "name": "E-commerce Product Catalog",
    "baseSelector": "div.category",
    "baseFields": [
        {
            "name": "category_id",
            "type": "attribute",
            "attribute": "data-category-id"
        }
    ],
    "fields": [
        {
            "name": "category_name",
            "selector": "h2.category-title",
            "type": "text"
        },
        {
            "name": "products",
            "selector": "div.product",
            "type": "nested_list",  # Array of complex objects
            "fields": [
                {
                    "name": "name",
                    "selector": "h3.product-name", 
                    "type": "text"
                },
                {
                    "name": "price",
                    "selector": "span.price",
                    "type": "text"
                },
                {
                    "name": "details",
                    "selector": "div.product-details",
                    "type": "nested",  # Single complex object
                    "fields": [
                        {
                            "name": "brand",
                            "selector": "span.brand",
                            "type": "text"
                        },
                        {
                            "name": "model",
                            "selector": "span.model",
                            "type": "text"
                        }
                    ]
                },
                {
                    "name": "features",
                    "selector": "ul.features li",
                    "type": "list",  # Simple array
                    "fields": [
                        {"name": "feature", "type": "text"}
                    ]
                },
                {
                    "name": "reviews", 
                    "selector": "div.review",
                    "type": "nested_list",
                    "fields": [
                        {
                            "name": "reviewer",
                            "selector": "span.reviewer-name",
                            "type": "text"
                        },
                        {
                            "name": "rating",
                            "selector": "span.rating",
                            "type": "attribute",
                            "attribute": "data-rating"
                        }
                    ]
                }
            ]
        }
    ]
}

async def extract_complex_ecommerce():
    strategy = JsonCssExtractionStrategy(complex_schema, verbose=True)
    config = CrawlerRunConfig(
        extraction_strategy=strategy,
        js_code="window.scrollTo(0, document.body.scrollHeight);",  # Load dynamic content
        wait_for="css:.product:nth-child(10)"  # Wait for products to load
    )
    
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url="https://example.com/complex-catalog",
            config=config
        )
        
        if result.success:
            data = json.loads(result.extracted_content)
            for category in data:
                print(f"Category: {category['category_name']}")
                print(f"Products: {len(category.get('products', []))}")

asyncio.run(extract_complex_ecommerce())
```

### XPath Alternative (When CSS Isn't Enough)

```python
from crawl4ai import JsonXPathExtractionStrategy

# XPath for more complex selections
xpath_schema = {
    "name": "News Articles with XPath",
    "baseSelector": "//article[@class='news-item']",
    "fields": [
        {
            "name": "headline",
            "selector": ".//h2[contains(@class, 'headline')]",
            "type": "text"
        },
        {
            "name": "author",
            "selector": ".//span[@class='author']/text()",
            "type": "text"
        },
        {
            "name": "publish_date",
            "selector": ".//time/@datetime",
            "type": "text"
        },
        {
            "name": "content",
            "selector": ".//div[@class='article-body']//text()",
            "type": "text"
        }
    ]
}

strategy = JsonXPathExtractionStrategy(xpath_schema, verbose=True)
```

---

## 3. Regex Extraction - Lightning Fast Pattern Matching

**Use this for**: Simple data types like emails, phones, URLs, prices, dates.

### Built-in Patterns (Fastest Option)

```python
import json
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai import RegexExtractionStrategy

async def extract_common_patterns():
    # Use built-in patterns for common data types
    strategy = RegexExtractionStrategy(
        pattern=(
            RegexExtractionStrategy.Email |
            RegexExtractionStrategy.PhoneUS |
            RegexExtractionStrategy.Url |
            RegexExtractionStrategy.Currency |
            RegexExtractionStrategy.DateIso
        )
    )
    
    config = CrawlerRunConfig(extraction_strategy=strategy)
    
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url="https://example.com/contact",
            config=config
        )
        
        if result.success:
            matches = json.loads(result.extracted_content)
            
            # Group by pattern type
            by_type = {}
            for match in matches:
                label = match['label']
                if label not in by_type:
                    by_type[label] = []
                by_type[label].append(match['value'])
            
            for pattern_type, values in by_type.items():
                print(f"{pattern_type}: {len(values)} matches")
                for value in values[:3]:
                    print(f"  {value}")

asyncio.run(extract_common_patterns())
```

### Available Built-in Patterns

```python
# Individual patterns
RegexExtractionStrategy.Email          # Email addresses
RegexExtractionStrategy.PhoneUS        # US phone numbers 
RegexExtractionStrategy.PhoneIntl      # International phones
RegexExtractionStrategy.Url            # HTTP/HTTPS URLs
RegexExtractionStrategy.Currency       # Currency values ($99.99)
RegexExtractionStrategy.Percentage     # Percentage values (25%)
RegexExtractionStrategy.DateIso        # ISO dates (2024-01-01)
RegexExtractionStrategy.DateUS         # US dates (01/01/2024)
RegexExtractionStrategy.IPv4           # IP addresses
RegexExtractionStrategy.CreditCard     # Credit card numbers
RegexExtractionStrategy.TwitterHandle  # @username
RegexExtractionStrategy.Hashtag        # #hashtag

# Use all patterns
RegexExtractionStrategy.All
```

### Custom Patterns

```python
# Custom patterns for specific data types
async def extract_custom_patterns():
    custom_patterns = {
        "product_sku": r"SKU[-:]?\s*([A-Z0-9]{4,12})",
        "discount": r"(\d{1,2})%\s*off",
        "model_number": r"Model\s*#?\s*([A-Z0-9-]+)",
        "isbn": r"ISBN[-:]?\s*(\d{10}|\d{13})",
        "stock_ticker": r"\$([A-Z]{2,5})",
        "version": r"v(\d+\.\d+(?:\.\d+)?)"
    }
    
    strategy = RegexExtractionStrategy(custom=custom_patterns)
    config = CrawlerRunConfig(extraction_strategy=strategy)
    
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url="https://example.com/products",
            config=config
        )
        
        if result.success:
            data = json.loads(result.extracted_content)
            for item in data:
                print(f"{item['label']}: {item['value']}")

asyncio.run(extract_custom_patterns())
```

### LLM-Generated Patterns (One-Time Cost)

```python
async def generate_optimized_regex():
    """
    Use LLM ONCE to generate optimized regex patterns
    Then use them unlimited times with zero LLM calls
    """
    cache_file = Path("./patterns/price_patterns.json")
    
    if cache_file.exists():
        # Load cached patterns - NO LLM CALLS
        patterns = json.load(cache_file.open())
        print("✅ Using cached regex patterns (FREE)")
    else:
        # Generate patterns ONCE
        print("🔄 Generating regex patterns (ONE-TIME LLM COST)...")
        
        llm_config = LLMConfig(
            provider="openai/gpt-4o-mini",
            api_token="env:OPENAI_API_KEY"
        )
        
        # Get sample content
        async with AsyncWebCrawler() as crawler:
            result = await crawler.arun("https://example.com/pricing")
            sample_html = result.cleaned_html
        
        # Generate optimized patterns
        patterns = RegexExtractionStrategy.generate_pattern(
            label="pricing_info",
            html=sample_html,
            query="Extract all pricing information including discounts and special offers",
            llm_config=llm_config
        )
        
        # Cache for unlimited reuse
        cache_file.parent.mkdir(exist_ok=True)
        json.dump(patterns, cache_file.open("w"), indent=2)
        print("✅ Patterns generated and cached")
    
    # Use cached patterns (NO MORE LLM CALLS)
    strategy = RegexExtractionStrategy(custom=patterns)
    return strategy

# Use generated patterns for unlimited extractions
strategy = await generate_optimized_regex()
```

---

## 4. Multi-Strategy Extraction Pipeline

**Combine strategies** for comprehensive data extraction:

```python
async def multi_strategy_pipeline():
    """
    Efficient pipeline using multiple non-LLM strategies:
    1. Regex for simple patterns (fastest)
    2. Schema for structured data 
    3. Only use LLM if absolutely necessary
    """
    
    url = "https://example.com/complex-page"
    
    async with AsyncWebCrawler() as crawler:
        # Strategy 1: Fast regex for contact info
        regex_strategy = RegexExtractionStrategy(
            pattern=RegexExtractionStrategy.Email | RegexExtractionStrategy.PhoneUS
        )
        regex_config = CrawlerRunConfig(extraction_strategy=regex_strategy)
        regex_result = await crawler.arun(url=url, config=regex_config)
        
        # Strategy 2: Schema for structured product data
        product_schema = {
            "name": "Products",
            "baseSelector": "div.product",
            "fields": [
                {"name": "name", "selector": "h3", "type": "text"},
                {"name": "price", "selector": ".price", "type": "text"}
            ]
        }
        css_strategy = JsonCssExtractionStrategy(product_schema)
        css_config = CrawlerRunConfig(extraction_strategy=css_strategy)
        css_result = await crawler.arun(url=url, config=css_config)
        
        # Combine results
        results = {
            "contacts": json.loads(regex_result.extracted_content) if regex_result.success else [],
            "products": json.loads(css_result.extracted_content) if css_result.success else []
        }
        
        print(f"✅ Extracted {len(results['contacts'])} contacts (regex)")
        print(f"✅ Extracted {len(results['products'])} products (schema)")
        
        return results

asyncio.run(multi_strategy_pipeline())
```

---

## 5. Performance Optimization Tips

### Caching and Reuse

```python
# Cache schemas and patterns for maximum efficiency
class ExtractionCache:
    def __init__(self):
        self.schemas = {}
        self.patterns = {}
    
    def get_schema(self, site_name):
        if site_name not in self.schemas:
            schema_file = Path(f"./cache/{site_name}_schema.json")
            if schema_file.exists():
                self.schemas[site_name] = json.load(schema_file.open())
        return self.schemas.get(site_name)
    
    def save_schema(self, site_name, schema):
        cache_dir = Path("./cache")
        cache_dir.mkdir(exist_ok=True)
        schema_file = cache_dir / f"{site_name}_schema.json"
        json.dump(schema, schema_file.open("w"), indent=2)
        self.schemas[site_name] = schema

cache = ExtractionCache()

# Reuse cached schemas across multiple extractions
async def efficient_extraction():
    sites = ["amazon", "ebay", "shopify"]
    
    for site in sites:
        schema = cache.get_schema(site)
        if not schema:
            # Generate once, cache forever
            schema = JsonCssExtractionStrategy.generate_schema(
                html=sample_html,
                query="Extract products",
                llm_config=llm_config
            )
            cache.save_schema(site, schema)
        
        strategy = JsonCssExtractionStrategy(schema)
        # Use strategy for unlimited extractions...
```

### Selector Optimization

```python
# Optimize selectors for speed
fast_schema = {
    "name": "Optimized Extraction",
    "baseSelector": "#products > .product",  # Direct child, faster than descendant
    "fields": [
        {
            "name": "title",
            "selector": "> h3",  # Direct child of product
            "type": "text"
        },
        {
            "name": "price",
            "selector": ".price:first-child",  # More specific
            "type": "text"
        }
    ]
}

# Avoid slow selectors
slow_schema = {
    "baseSelector": "div div div .product",  # Too many levels
    "fields": [
        {
            "selector": "* h3",  # Universal selector is slow
            "type": "text"
        }
    ]
}
```

---

## 6. Error Handling and Validation

```python
async def robust_extraction():
    """
    Implement fallback strategies for reliable extraction
    """
    strategies = [
        # Try fast regex first
        RegexExtractionStrategy(pattern=RegexExtractionStrategy.Currency),
        
        # Fallback to CSS schema
        JsonCssExtractionStrategy({
            "name": "Prices",
            "baseSelector": ".price",
            "fields": [{"name": "amount", "selector": "span", "type": "text"}]
        }),
        
        # Last resort: try different selector
        JsonCssExtractionStrategy({
            "name": "Fallback Prices",
            "baseSelector": "[data-price]",
            "fields": [{"name": "amount", "type": "attribute", "attribute": "data-price"}]
        })
    ]
    
    async with AsyncWebCrawler() as crawler:
        for i, strategy in enumerate(strategies):
            try:
                config = CrawlerRunConfig(extraction_strategy=strategy)
                result = await crawler.arun(url="https://example.com", config=config)
                
                if result.success and result.extracted_content:
                    data = json.loads(result.extracted_content)
                    if data:  # Validate non-empty results
                        print(f"✅ Success with strategy {i+1}: {strategy.__class__.__name__}")
                        return data
                        
            except Exception as e:
                print(f"❌ Strategy {i+1} failed: {e}")
                continue
    
    print("❌ All strategies failed")
    return None

# Validate extracted data
def validate_extraction(data, required_fields):
    """Validate that extraction contains expected fields"""
    if not data or not isinstance(data, list):
        return False
    
    for item in data:
        for field in required_fields:
            if field not in item or not item[field]:
                return False
    return True

# Usage
result = await robust_extraction()
if validate_extraction(result, ["amount"]):
    print("✅ Extraction validated")
else:
    print("❌ Validation failed")
```

---

## 7. Common Extraction Patterns

### E-commerce Products

```python
ecommerce_schema = {
    "name": "E-commerce Products",
    "baseSelector": ".product, [data-product], .item",
    "fields": [
        {"name": "title", "selector": "h1, h2, h3, .title, .name", "type": "text"},
        {"name": "price", "selector": ".price, .cost, [data-price]", "type": "text"},
        {"name": "image", "selector": "img", "type": "attribute", "attribute": "src"},
        {"name": "url", "selector": "a", "type": "attribute", "attribute": "href"},
        {"name": "rating", "selector": ".rating, .stars", "type": "text"},
        {"name": "availability", "selector": ".stock, .availability", "type": "text"}
    ]
}
```

### News Articles

```python
news_schema = {
    "name": "News Articles",
    "baseSelector": "article, .article, .post",
    "fields": [
        {"name": "headline", "selector": "h1, h2, .headline, .title", "type": "text"},
        {"name": "author", "selector": ".author, .byline, [rel='author']", "type": "text"},
        {"name": "date", "selector": "time, .date, .published", "type": "text"},
        {"name": "content", "selector": ".content, .body, .text", "type": "text"},
        {"name": "category", "selector": ".category, .section", "type": "text"}
    ]
}
```

### Job Listings

```python
job_schema = {
    "name": "Job Listings",
    "baseSelector": ".job, .listing, [data-job]",
    "fields": [
        {"name": "title", "selector": ".job-title, h2, h3", "type": "text"},
        {"name": "company", "selector": ".company, .employer", "type": "text"},
        {"name": "location", "selector": ".location, .place", "type": "text"},
        {"name": "salary", "selector": ".salary, .pay, .compensation", "type": "text"},
        {"name": "description", "selector": ".description, .summary", "type": "text"},
        {"name": "url", "selector": "a", "type": "attribute", "attribute": "href"}
    ]
}
```

### Social Media Posts

```python
social_schema = {
    "name": "Social Media Posts",
    "baseSelector": ".post, .tweet, .update",
    "fields": [
        {"name": "username", "selector": ".username, .handle, .author", "type": "text"},
        {"name": "content", "selector": ".content, .text, .message", "type": "text"},
        {"name": "timestamp", "selector": ".time, .date, time", "type": "text"},
        {"name": "likes", "selector": ".likes, .hearts", "type": "text"},
        {"name": "shares", "selector": ".shares, .retweets", "type": "text"}
    ]
}
```

---

## 8. When to (Rarely) Consider LLM

**⚠️ WARNING: Before considering LLM, ask yourself:**

1. "Can I identify repeating HTML patterns?" → Use CSS/XPath schema
2. "Am I extracting simple data types?" → Use Regex patterns  
3. "Can I provide a JSON example of what I want?" → Use generate_schema()
4. "Is this truly unstructured text requiring semantic understanding?" → Maybe LLM

**Only use LLM extraction for:**
- Unstructured prose that needs semantic analysis
- Content where structure varies dramatically across pages
- When you need AI reasoning about context/meaning

**Cost reminder**: LLM extraction costs 10,000x more than schema-based extraction.

---

## 9. Summary: The Extraction Hierarchy

1. **🥇 FIRST CHOICE**: `generate_schema()` - AI generates pattern once, use unlimited times
2. **🥈 SECOND CHOICE**: Manual CSS/XPath - Full control, maximum speed
3. **🥉 THIRD CHOICE**: Regex patterns - Simple data types, lightning fast
4. **🏴 LAST RESORT**: LLM extraction - Only for semantic reasoning

**Remember**: 99% of web data is structured. You almost never need LLM for extraction. Save LLM for analysis, not extraction.

**Performance**: Non-LLM strategies are 100-1000x faster and 10,000x cheaper than LLM extraction.

---

**📖 Next**: If you absolutely must use LLM extraction, see [extraction-llm.md](./extraction-llm.md) for guidance on the rare cases where it's justified.

---


## Data Extraction Without LLM - Diagrams & Workflows
Component ID: extraction-no-llm
Context Type: reasoning
Estimated tokens: 3,543

## Extraction Strategy Workflows and Architecture

Visual representations of Crawl4AI's data extraction approaches, strategy selection, and processing workflows.

### Extraction Strategy Decision Tree

```mermaid
flowchart TD
    A[Content to Extract] --> B{Content Type?}
    
    B -->|Simple Patterns| C[Common Data Types]
    B -->|Structured HTML| D[Predictable Structure]
    B -->|Complex Content| E[Requires Reasoning]
    B -->|Mixed Content| F[Multiple Data Types]
    
    C --> C1{Pattern Type?}
    C1 -->|Email, Phone, URLs| C2[Built-in Regex Patterns]
    C1 -->|Custom Patterns| C3[Custom Regex Strategy]
    C1 -->|LLM-Generated| C4[One-time Pattern Generation]
    
    D --> D1{Selector Type?}
    D1 -->|CSS Selectors| D2[JsonCssExtractionStrategy]
    D1 -->|XPath Expressions| D3[JsonXPathExtractionStrategy]
    D1 -->|Need Schema?| D4[Auto-generate Schema with LLM]
    
    E --> E1{LLM Provider?}
    E1 -->|OpenAI/Anthropic| E2[Cloud LLM Strategy]
    E1 -->|Local Ollama| E3[Local LLM Strategy]
    E1 -->|Cost-sensitive| E4[Hybrid: Generate Schema Once]
    
    F --> F1[Multi-Strategy Approach]
    F1 --> F2[1. Regex for Patterns]
    F1 --> F3[2. CSS for Structure]
    F1 --> F4[3. LLM for Complex Analysis]
    
    C2 --> G[Fast Extraction ⚡]
    C3 --> G
    C4 --> H[Cached Pattern Reuse]
    
    D2 --> I[Schema-based Extraction 🏗️]
    D3 --> I
    D4 --> J[Generated Schema Cache]
    
    E2 --> K[Intelligent Parsing 🧠]
    E3 --> K
    E4 --> L[Hybrid Cost-Effective]
    
    F2 --> M[Comprehensive Results 📊]
    F3 --> M
    F4 --> M
    
    style G fill:#c8e6c9
    style I fill:#e3f2fd
    style K fill:#fff3e0
    style M fill:#f3e5f5
    style H fill:#e8f5e8
    style J fill:#e8f5e8
    style L fill:#ffecb3
```

### LLM Extraction Strategy Workflow

```mermaid
sequenceDiagram
    participant User
    participant Crawler
    participant LLMStrategy
    participant Chunker
    participant LLMProvider
    participant Parser
    
    User->>Crawler: Configure LLMExtractionStrategy
    User->>Crawler: arun(url, config)
    
    Crawler->>Crawler: Navigate to URL
    Crawler->>Crawler: Extract content (HTML/Markdown)
    Crawler->>LLMStrategy: Process content
    
    LLMStrategy->>LLMStrategy: Check content size
    
    alt Content > chunk_threshold
        LLMStrategy->>Chunker: Split into chunks with overlap
        Chunker-->>LLMStrategy: Return chunks[]
        
        loop For each chunk
            LLMStrategy->>LLMProvider: Send chunk + schema + instruction
            LLMProvider-->>LLMStrategy: Return structured JSON
        end
        
        LLMStrategy->>LLMStrategy: Merge chunk results
    else Content <= threshold
        LLMStrategy->>LLMProvider: Send full content + schema
        LLMProvider-->>LLMStrategy: Return structured JSON
    end
    
    LLMStrategy->>Parser: Validate JSON schema
    Parser-->>LLMStrategy: Validated data
    
    LLMStrategy->>LLMStrategy: Track token usage
    LLMStrategy-->>Crawler: Return extracted_content
    
    Crawler-->>User: CrawlResult with JSON data
    
    User->>LLMStrategy: show_usage()
    LLMStrategy-->>User: Token count & estimated cost
```

### Schema-Based Extraction Architecture

```mermaid
graph TB
    subgraph "Schema Definition"
        A[JSON Schema] --> A1[baseSelector]
        A --> A2[fields[]]
        A --> A3[nested structures]
        
        A2 --> A4[CSS/XPath selectors]
        A2 --> A5[Data types: text, html, attribute]
        A2 --> A6[Default values]
        
        A3 --> A7[nested objects]
        A3 --> A8[nested_list arrays]
        A3 --> A9[simple lists]
    end
    
    subgraph "Extraction Engine"
        B[HTML Content] --> C[Selector Engine]
        C --> C1[CSS Selector Parser]
        C --> C2[XPath Evaluator]
        
        C1 --> D[Element Matcher]
        C2 --> D
        
        D --> E[Type Converter]
        E --> E1[Text Extraction]
        E --> E2[HTML Preservation]
        E --> E3[Attribute Extraction]
        E --> E4[Nested Processing]
    end
    
    subgraph "Result Processing"
        F[Raw Extracted Data] --> G[Structure Builder]
        G --> G1[Object Construction]
        G --> G2[Array Assembly]
        G --> G3[Type Validation]
        
        G1 --> H[JSON Output]
        G2 --> H
        G3 --> H
    end
    
    A --> C
    E --> F
    H --> I[extracted_content]
    
    style A fill:#e3f2fd
    style C fill:#f3e5f5
    style G fill:#e8f5e8
    style H fill:#c8e6c9
```

### Automatic Schema Generation Process

```mermaid
stateDiagram-v2
    [*] --> CheckCache
    
    CheckCache --> CacheHit: Schema exists
    CheckCache --> SamplePage: Schema missing
    
    CacheHit --> LoadSchema
    LoadSchema --> FastExtraction
    
    SamplePage --> ExtractHTML: Crawl sample URL
    ExtractHTML --> LLMAnalysis: Send HTML to LLM
    LLMAnalysis --> GenerateSchema: Create CSS/XPath selectors
    GenerateSchema --> ValidateSchema: Test generated schema
    
    ValidateSchema --> SchemaWorks: Valid selectors
    ValidateSchema --> RefineSchema: Invalid selectors
    
    RefineSchema --> LLMAnalysis: Iterate with feedback
    
    SchemaWorks --> CacheSchema: Save for reuse
    CacheSchema --> FastExtraction: Use cached schema
    
    FastExtraction --> [*]: No more LLM calls needed
    
    note right of CheckCache : One-time LLM cost
    note right of FastExtraction : Unlimited fast reuse
    note right of CacheSchema : JSON file storage
```

### Multi-Strategy Extraction Pipeline

```mermaid
flowchart LR
    A[Web Page Content] --> B[Strategy Pipeline]
    
    subgraph B["Extraction Pipeline"]
        B1[Stage 1: Regex Patterns]
        B2[Stage 2: Schema-based CSS]
        B3[Stage 3: LLM Analysis]
        
        B1 --> B1a[Email addresses]
        B1 --> B1b[Phone numbers]
        B1 --> B1c[URLs and links]
        B1 --> B1d[Currency amounts]
        
        B2 --> B2a[Structured products]
        B2 --> B2b[Article metadata]
        B2 --> B2c[User reviews]
        B2 --> B2d[Navigation links]
        
        B3 --> B3a[Sentiment analysis]
        B3 --> B3b[Key topics]
        B3 --> B3c[Entity recognition]
        B3 --> B3d[Content summary]
    end
    
    B1a --> C[Result Merger]
    B1b --> C
    B1c --> C
    B1d --> C
    
    B2a --> C
    B2b --> C
    B2c --> C
    B2d --> C
    
    B3a --> C
    B3b --> C
    B3c --> C
    B3d --> C
    
    C --> D[Combined JSON Output]
    D --> E[Final CrawlResult]
    
    style B1 fill:#c8e6c9
    style B2 fill:#e3f2fd
    style B3 fill:#fff3e0
    style C fill:#f3e5f5
```

### Performance Comparison Matrix

```mermaid
graph TD
    subgraph "Strategy Performance"
        A[Extraction Strategy Comparison]
        
        subgraph "Speed ⚡"
            S1[Regex: ~10ms]
            S2[CSS Schema: ~50ms]
            S3[XPath: ~100ms]
            S4[LLM: ~2-10s]
        end
        
        subgraph "Accuracy 🎯"
            A1[Regex: Pattern-dependent]
            A2[CSS: High for structured]
            A3[XPath: Very high]
            A4[LLM: Excellent for complex]
        end
        
        subgraph "Cost 💰"
            C1[Regex: Free]
            C2[CSS: Free]
            C3[XPath: Free]
            C4[LLM: $0.001-0.01 per page]
        end
        
        subgraph "Complexity 🔧"
            X1[Regex: Simple patterns only]
            X2[CSS: Structured HTML]
            X3[XPath: Complex selectors]
            X4[LLM: Any content type]
        end
    end
    
    style S1 fill:#c8e6c9
    style S2 fill:#e8f5e8
    style S3 fill:#fff3e0
    style S4 fill:#ffcdd2
    
    style A2 fill:#e8f5e8
    style A3 fill:#c8e6c9
    style A4 fill:#c8e6c9
    
    style C1 fill:#c8e6c9
    style C2 fill:#c8e6c9
    style C3 fill:#c8e6c9
    style C4 fill:#fff3e0
    
    style X1 fill:#ffcdd2
    style X2 fill:#e8f5e8
    style X3 fill:#c8e6c9
    style X4 fill:#c8e6c9
```

### Regex Pattern Strategy Flow

```mermaid
flowchart TD
    A[Regex Extraction] --> B{Pattern Source?}
    
    B -->|Built-in| C[Use Predefined Patterns]
    B -->|Custom| D[Define Custom Regex]
    B -->|LLM-Generated| E[Generate with AI]
    
    C --> C1[Email Pattern]
    C --> C2[Phone Pattern]
    C --> C3[URL Pattern]
    C --> C4[Currency Pattern]
    C --> C5[Date Pattern]
    
    D --> D1[Write Custom Regex]
    D --> D2[Test Pattern]
    D --> D3{Pattern Works?}
    D3 -->|No| D1
    D3 -->|Yes| D4[Use Pattern]
    
    E --> E1[Provide Sample Content]
    E --> E2[LLM Analyzes Content]
    E --> E3[Generate Optimized Regex]
    E --> E4[Cache Pattern for Reuse]
    
    C1 --> F[Pattern Matching]
    C2 --> F
    C3 --> F
    C4 --> F
    C5 --> F
    D4 --> F
    E4 --> F
    
    F --> G[Extract Matches]
    G --> H[Group by Pattern Type]
    H --> I[JSON Output with Labels]
    
    style C fill:#e8f5e8
    style D fill:#e3f2fd
    style E fill:#fff3e0
    style F fill:#f3e5f5
```

### Complex Schema Structure Visualization

```mermaid
graph TB
    subgraph "E-commerce Schema Example"
        A[Category baseSelector] --> B[Category Fields]
        A --> C[Products nested_list]
        
        B --> B1[category_name]
        B --> B2[category_id attribute]
        B --> B3[category_url attribute]
        
        C --> C1[Product baseSelector]
        C1 --> C2[name text]
        C1 --> C3[price text]
        C1 --> C4[Details nested object]
        C1 --> C5[Features list]
        C1 --> C6[Reviews nested_list]
        
        C4 --> C4a[brand text]
        C4 --> C4b[model text]
        C4 --> C4c[specs html]
        
        C5 --> C5a[feature text array]
        
        C6 --> C6a[reviewer text]
        C6 --> C6b[rating attribute]
        C6 --> C6c[comment text]
        C6 --> C6d[date attribute]
    end
    
    subgraph "JSON Output Structure"
        D[categories array] --> D1[category object]
        D1 --> D2[category_name]
        D1 --> D3[category_id]
        D1 --> D4[products array]
        
        D4 --> D5[product object]
        D5 --> D6[name, price]
        D5 --> D7[details object]
        D5 --> D8[features array]
        D5 --> D9[reviews array]
        
        D7 --> D7a[brand, model, specs]
        D8 --> D8a[feature strings]
        D9 --> D9a[review objects]
    end
    
    A -.-> D
    B1 -.-> D2
    C2 -.-> D6
    C4 -.-> D7
    C5 -.-> D8
    C6 -.-> D9
    
    style A fill:#e3f2fd
    style C fill:#f3e5f5
    style C4 fill:#e8f5e8
    style D fill:#fff3e0
```

### Error Handling and Fallback Strategy

```mermaid
stateDiagram-v2
    [*] --> PrimaryStrategy
    
    PrimaryStrategy --> Success: Extraction successful
    PrimaryStrategy --> ValidationFailed: Invalid data
    PrimaryStrategy --> ExtractionFailed: No matches found
    PrimaryStrategy --> TimeoutError: LLM timeout
    
    ValidationFailed --> FallbackStrategy: Try alternative
    ExtractionFailed --> FallbackStrategy: Try alternative
    TimeoutError --> FallbackStrategy: Try alternative
    
    FallbackStrategy --> FallbackSuccess: Fallback works
    FallbackStrategy --> FallbackFailed: All strategies failed
    
    FallbackSuccess --> Success: Return results
    FallbackFailed --> ErrorReport: Log failure details
    
    Success --> [*]: Complete
    ErrorReport --> [*]: Return empty results
    
    note right of PrimaryStrategy : Try fastest/most accurate first
    note right of FallbackStrategy : Use simpler but reliable method
    note left of ErrorReport : Provide debugging information
```

### Token Usage and Cost Optimization

```mermaid
flowchart TD
    A[LLM Extraction Request] --> B{Content Size Check}
    
    B -->|Small < 1200 tokens| C[Single LLM Call]
    B -->|Large > 1200 tokens| D[Chunking Strategy]
    
    C --> C1[Send full content]
    C1 --> C2[Parse JSON response]
    C2 --> C3[Track token usage]
    
    D --> D1[Split into chunks]
    D1 --> D2[Add overlap between chunks]
    D2 --> D3[Process chunks in parallel]
    
    D3 --> D4[Chunk 1 → LLM]
    D3 --> D5[Chunk 2 → LLM]
    D3 --> D6[Chunk N → LLM]
    
    D4 --> D7[Merge results]
    D5 --> D7
    D6 --> D7
    
    D7 --> D8[Deduplicate data]
    D8 --> D9[Aggregate token usage]
    
    C3 --> E[Cost Calculation]
    D9 --> E
    
    E --> F[Usage Report]
    F --> F1[Prompt tokens: X]
    F --> F2[Completion tokens: Y]
    F --> F3[Total cost: $Z]
    
    style C fill:#c8e6c9
    style D fill:#fff3e0
    style E fill:#e3f2fd
    style F fill:#f3e5f5
```

**📖 Learn more:** [LLM Strategies](https://docs.crawl4ai.com/extraction/llm-strategies/), [Schema-Based Extraction](https://docs.crawl4ai.com/extraction/no-llm-strategies/), [Pattern Matching](https://docs.crawl4ai.com/extraction/no-llm-strategies/#regexextractionstrategy), [Performance Optimization](https://docs.crawl4ai.com/advanced/multi-url-crawling/)

---


## HTTP-based Crawler - Full Content
Component ID: http_based_crawler_strategy
Context Type: memory
Estimated tokens: 2,390

## HTTP Crawler Strategy

Fast, lightweight HTTP-only crawling without browser overhead for cases where JavaScript execution isn't needed.

### Basic HTTP Crawler Setup

```python
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, HTTPCrawlerConfig, CacheMode
from crawl4ai.async_crawler_strategy import AsyncHTTPCrawlerStrategy
from crawl4ai.async_logger import AsyncLogger

async def main():
    # Initialize HTTP strategy
    http_strategy = AsyncHTTPCrawlerStrategy(
        browser_config=HTTPCrawlerConfig(
            method="GET",
            verify_ssl=True,
            follow_redirects=True
        ),
        logger=AsyncLogger(verbose=True)
    )

    # Use with AsyncWebCrawler
    async with AsyncWebCrawler(crawler_strategy=http_strategy) as crawler:
        result = await crawler.arun("https://example.com")
        print(f"Status: {result.status_code}")
        print(f"Content: {len(result.html)} chars")

if __name__ == "__main__":
    asyncio.run(main())
```

### HTTP Request Types

```python
# GET request (default)
http_config = HTTPCrawlerConfig(
    method="GET",
    headers={"Accept": "application/json"}
)

# POST with JSON data
http_config = HTTPCrawlerConfig(
    method="POST",
    json={"key": "value", "data": [1, 2, 3]},
    headers={"Content-Type": "application/json"}
)

# POST with form data
http_config = HTTPCrawlerConfig(
    method="POST",
    data={"username": "user", "password": "pass"},
    headers={"Content-Type": "application/x-www-form-urlencoded"}
)

# Advanced configuration
http_config = HTTPCrawlerConfig(
    method="GET",
    headers={"User-Agent": "Custom Bot/1.0"},
    follow_redirects=True,
    verify_ssl=False  # For testing environments
)

strategy = AsyncHTTPCrawlerStrategy(browser_config=http_config)
```

### File and Raw Content Handling

```python
async def test_content_types():
    strategy = AsyncHTTPCrawlerStrategy()
    
    # Web URLs
    result = await strategy.crawl("https://httpbin.org/get")
    print(f"Web content: {result.status_code}")
    
    # Local files
    result = await strategy.crawl("file:///path/to/local/file.html")
    print(f"File content: {len(result.html)}")
    
    # Raw HTML content
    raw_html = "raw://<html><body><h1>Test</h1><p>Content</p></body></html>"
    result = await strategy.crawl(raw_html)
    print(f"Raw content: {result.html}")
    
    # Raw content with complex HTML
    complex_html = """raw://<!DOCTYPE html>
    <html>
    <head><title>Test Page</title></head>
    <body>
        <div class="content">
            <h1>Main Title</h1>
            <p>Paragraph content</p>
            <ul><li>Item 1</li><li>Item 2</li></ul>
        </div>
    </body>
    </html>"""
    result = await strategy.crawl(complex_html)
```

### Custom Hooks and Request Handling

```python
async def setup_hooks():
    strategy = AsyncHTTPCrawlerStrategy()
    
    # Before request hook
    async def before_request(url, kwargs):
        print(f"Requesting: {url}")
        kwargs['headers']['X-Custom-Header'] = 'crawl4ai'
        kwargs['headers']['Authorization'] = 'Bearer token123'
    
    # After request hook
    async def after_request(response):
        print(f"Response: {response.status_code}")
        if hasattr(response, 'redirected_url'):
            print(f"Redirected to: {response.redirected_url}")
    
    # Error handling hook
    async def on_error(error):
        print(f"Request failed: {error}")
    
    # Set hooks
    strategy.set_hook('before_request', before_request)
    strategy.set_hook('after_request', after_request)
    strategy.set_hook('on_error', on_error)
    
    # Use with hooks
    result = await strategy.crawl("https://httpbin.org/headers")
    return result
```

### Performance Configuration

```python
# High-performance setup
strategy = AsyncHTTPCrawlerStrategy(
    max_connections=50,        # Concurrent connections
    dns_cache_ttl=300,        # DNS cache timeout
    chunk_size=128 * 1024     # 128KB chunks for large files
)

# Memory-efficient setup for large files
strategy = AsyncHTTPCrawlerStrategy(
    max_connections=10,
    chunk_size=32 * 1024,     # Smaller chunks
    dns_cache_ttl=600
)

# Custom timeout configuration
config = CrawlerRunConfig(
    page_timeout=30000,       # 30 second timeout
    cache_mode=CacheMode.BYPASS
)

result = await strategy.crawl("https://slow-server.com", config=config)
```

### Error Handling and Retries

```python
from crawl4ai.async_crawler_strategy import (
    ConnectionTimeoutError, 
    HTTPStatusError, 
    HTTPCrawlerError
)

async def robust_crawling():
    strategy = AsyncHTTPCrawlerStrategy()
    
    urls = [
        "https://example.com",
        "https://httpbin.org/status/404",
        "https://nonexistent.domain.test"
    ]
    
    for url in urls:
        try:
            result = await strategy.crawl(url)
            print(f"✓ {url}: {result.status_code}")
            
        except HTTPStatusError as e:
            print(f"✗ {url}: HTTP {e.status_code}")
            
        except ConnectionTimeoutError as e:
            print(f"✗ {url}: Timeout - {e}")
            
        except HTTPCrawlerError as e:
            print(f"✗ {url}: Crawler error - {e}")
            
        except Exception as e:
            print(f"✗ {url}: Unexpected error - {e}")

# Retry mechanism
async def crawl_with_retry(url, max_retries=3):
    strategy = AsyncHTTPCrawlerStrategy()
    
    for attempt in range(max_retries):
        try:
            return await strategy.crawl(url)
        except (ConnectionTimeoutError, HTTPCrawlerError) as e:
            if attempt == max_retries - 1:
                raise
            print(f"Retry {attempt + 1}/{max_retries}: {e}")
            await asyncio.sleep(2 ** attempt)  # Exponential backoff
```

### Batch Processing with HTTP Strategy

```python
async def batch_http_crawling():
    strategy = AsyncHTTPCrawlerStrategy(max_connections=20)
    
    urls = [
        "https://httpbin.org/get",
        "https://httpbin.org/user-agent",
        "https://httpbin.org/headers",
        "https://example.com",
        "https://httpbin.org/json"
    ]
    
    # Sequential processing
    results = []
    async with strategy:
        for url in urls:
            try:
                result = await strategy.crawl(url)
                results.append((url, result.status_code, len(result.html)))
            except Exception as e:
                results.append((url, "ERROR", str(e)))
    
    for url, status, content_info in results:
        print(f"{url}: {status} - {content_info}")

# Concurrent processing
async def concurrent_http_crawling():
    strategy = AsyncHTTPCrawlerStrategy()
    urls = ["https://httpbin.org/delay/1"] * 5
    
    async def crawl_single(url):
        try:
            result = await strategy.crawl(url)
            return f"✓ {result.status_code}"
        except Exception as e:
            return f"✗ {e}"
    
    async with strategy:
        tasks = [crawl_single(url) for url in urls]
        results = await asyncio.gather(*tasks, return_exceptions=True)
    
    for i, result in enumerate(results):
        print(f"URL {i+1}: {result}")
```

### Integration with Content Processing

```python
from crawl4ai import DefaultMarkdownGenerator, PruningContentFilter

async def http_with_processing():
    # HTTP strategy with content processing
    http_strategy = AsyncHTTPCrawlerStrategy(
        browser_config=HTTPCrawlerConfig(verify_ssl=True)
    )
    
    # Configure markdown generation
    crawler_config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        markdown_generator=DefaultMarkdownGenerator(
            content_filter=PruningContentFilter(
                threshold=0.48,
                threshold_type="fixed",
                min_word_threshold=10
            )
        ),
        word_count_threshold=5,
        excluded_tags=['script', 'style', 'nav'],
        exclude_external_links=True
    )
    
    async with AsyncWebCrawler(crawler_strategy=http_strategy) as crawler:
        result = await crawler.arun(
            url="https://example.com",
            config=crawler_config
        )
        
        print(f"Status: {result.status_code}")
        print(f"Raw HTML: {len(result.html)} chars")
        if result.markdown:
            print(f"Markdown: {len(result.markdown.raw_markdown)} chars")
            if result.markdown.fit_markdown:
                print(f"Filtered: {len(result.markdown.fit_markdown)} chars")
```

### HTTP vs Browser Strategy Comparison

```python
async def strategy_comparison():
    # Same URL with different strategies
    url = "https://example.com"
    
    # HTTP Strategy (fast, no JS)
    http_strategy = AsyncHTTPCrawlerStrategy()
    start_time = time.time()
    http_result = await http_strategy.crawl(url)
    http_time = time.time() - start_time
    
    # Browser Strategy (full features)
    from crawl4ai import BrowserConfig
    browser_config = BrowserConfig(headless=True)
    start_time = time.time()
    async with AsyncWebCrawler(config=browser_config) as crawler:
        browser_result = await crawler.arun(url)
    browser_time = time.time() - start_time
    
    print(f"HTTP Strategy:")
    print(f"  Time: {http_time:.2f}s")
    print(f"  Content: {len(http_result.html)} chars")
    print(f"  Features: Fast, lightweight, no JS")
    
    print(f"Browser Strategy:")
    print(f"  Time: {browser_time:.2f}s") 
    print(f"  Content: {len(browser_result.html)} chars")
    print(f"  Features: Full browser, JS, screenshots, etc.")
    
    # When to use HTTP strategy:
    # - Static content sites
    # - APIs returning HTML
    # - Fast bulk processing
    # - No JavaScript required
    # - Memory/resource constraints
    
    # When to use Browser strategy:
    # - Dynamic content (SPA, AJAX)
    # - JavaScript-heavy sites
    # - Screenshots/PDFs needed
    # - Complex interactions required
```

### Advanced Configuration

```python
# Custom session configuration
import aiohttp

async def advanced_http_setup():
    # Custom connector with specific settings
    connector = aiohttp.TCPConnector(
        limit=100,              # Connection pool size
        ttl_dns_cache=600,      # DNS cache TTL
        use_dns_cache=True,     # Enable DNS caching
        keepalive_timeout=30,   # Keep-alive timeout
        force_close=False       # Reuse connections
    )
    
    strategy = AsyncHTTPCrawlerStrategy(
        max_connections=50,
        dns_cache_ttl=600,
        chunk_size=64 * 1024
    )
    
    # Custom headers for all requests
    http_config = HTTPCrawlerConfig(
        headers={
            "User-Agent": "Crawl4AI-HTTP/1.0",
            "Accept": "text/html,application/xhtml+xml",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "DNT": "1"
        },
        verify_ssl=True,
        follow_redirects=True
    )
    
    strategy.browser_config = http_config
    
    # Use with custom timeout
    config = CrawlerRunConfig(
        page_timeout=45000,  # 45 seconds
        cache_mode=CacheMode.ENABLED
    )
    
    result = await strategy.crawl("https://example.com", config=config)
    await strategy.close()
```

**📖 Learn more:** [AsyncWebCrawler API](https://docs.crawl4ai.com/api/async-webcrawler/), [Browser vs HTTP Strategy](https://docs.crawl4ai.com/core/browser-crawler-config/), [Performance Optimization](https://docs.crawl4ai.com/advanced/multi-url-crawling/)

---


## HTTP-based Crawler - Diagrams & Workflows
Component ID: http_based_crawler_strategy
Context Type: reasoning
Estimated tokens: 3,413

## HTTP Crawler Strategy Workflows

Visual representations of HTTP-based crawling architecture, request flows, and performance characteristics compared to browser-based strategies.

### HTTP vs Browser Strategy Decision Tree

```mermaid
flowchart TD
    A[Content Crawling Need] --> B{Content Type Analysis}
    
    B -->|Static HTML| C{JavaScript Required?}
    B -->|Dynamic SPA| D[Browser Strategy Required]
    B -->|API Endpoints| E[HTTP Strategy Optimal]
    B -->|Mixed Content| F{Primary Content Source?}
    
    C -->|No JS Needed| G[HTTP Strategy Recommended]
    C -->|JS Required| H[Browser Strategy Required]
    C -->|Unknown| I{Performance Priority?}
    
    I -->|Speed Critical| J[Try HTTP First]
    I -->|Accuracy Critical| K[Use Browser Strategy]
    
    F -->|Mostly Static| G
    F -->|Mostly Dynamic| D
    
    G --> L{Resource Constraints?}
    L -->|Memory Limited| M[HTTP Strategy - Lightweight]
    L -->|CPU Limited| N[HTTP Strategy - No Browser]
    L -->|Network Limited| O[HTTP Strategy - Efficient]
    L -->|No Constraints| P[Either Strategy Works]
    
    J --> Q[Test HTTP Results]
    Q --> R{Content Complete?}
    R -->|Yes| S[Continue with HTTP]
    R -->|No| T[Switch to Browser Strategy]
    
    D --> U[Browser Strategy Features]
    H --> U
    K --> U
    T --> U
    
    U --> V[JavaScript Execution]
    U --> W[Screenshots/PDFs]
    U --> X[Complex Interactions]
    U --> Y[Session Management]
    
    M --> Z[HTTP Strategy Benefits]
    N --> Z
    O --> Z
    S --> Z
    
    Z --> AA[10x Faster Processing]
    Z --> BB[Lower Memory Usage]
    Z --> CC[Higher Concurrency]
    Z --> DD[Simpler Deployment]
    
    style G fill:#c8e6c9
    style M fill:#c8e6c9
    style N fill:#c8e6c9
    style O fill:#c8e6c9
    style S fill:#c8e6c9
    style D fill:#e3f2fd
    style H fill:#e3f2fd
    style K fill:#e3f2fd
    style T fill:#e3f2fd
    style U fill:#e3f2fd
```

### HTTP Request Lifecycle Sequence

```mermaid
sequenceDiagram
    participant Client
    participant HTTPStrategy as HTTP Strategy
    participant Session as HTTP Session
    participant Server as Target Server
    participant Processor as Content Processor
    
    Client->>HTTPStrategy: crawl(url, config)
    HTTPStrategy->>HTTPStrategy: validate_url()
    
    alt URL Type Check
        HTTPStrategy->>HTTPStrategy: handle_file_url()
        Note over HTTPStrategy: file:// URLs
    else
        HTTPStrategy->>HTTPStrategy: handle_raw_content()
        Note over HTTPStrategy: raw:// content
    else
        HTTPStrategy->>Session: prepare_request()
        Session->>Session: apply_config()
        Session->>Session: set_headers()
        Session->>Session: setup_auth()
        
        Session->>Server: HTTP Request
        Note over Session,Server: GET/POST/PUT with headers
        
        alt Success Response
            Server-->>Session: HTTP 200 + Content
            Session-->>HTTPStrategy: response_data
        else Redirect Response
            Server-->>Session: HTTP 3xx + Location
            Session->>Server: Follow redirect
            Server-->>Session: HTTP 200 + Content
            Session-->>HTTPStrategy: final_response
        else Error Response
            Server-->>Session: HTTP 4xx/5xx
            Session-->>HTTPStrategy: error_response
        end
    end
    
    HTTPStrategy->>Processor: process_content()
    Processor->>Processor: clean_html()
    Processor->>Processor: extract_metadata()
    Processor->>Processor: generate_markdown()
    Processor-->>HTTPStrategy: processed_result
    
    HTTPStrategy-->>Client: CrawlResult
    
    Note over Client,Processor: Fast, lightweight processing
    Note over HTTPStrategy: No browser overhead
```

### HTTP Strategy Architecture

```mermaid
graph TB
    subgraph "HTTP Crawler Strategy"
        A[AsyncHTTPCrawlerStrategy] --> B[Session Manager]
        A --> C[Request Builder]
        A --> D[Response Handler]
        A --> E[Error Manager]
        
        B --> B1[Connection Pool]
        B --> B2[DNS Cache]
        B --> B3[SSL Context]
        
        C --> C1[Headers Builder]
        C --> C2[Auth Handler]
        C --> C3[Payload Encoder]
        
        D --> D1[Content Decoder]
        D --> D2[Redirect Handler]
        D --> D3[Status Validator]
        
        E --> E1[Retry Logic]
        E --> E2[Timeout Handler]
        E --> E3[Exception Mapper]
    end
    
    subgraph "Content Processing"
        F[Raw HTML] --> G[HTML Cleaner]
        G --> H[Markdown Generator]
        H --> I[Link Extractor]
        I --> J[Media Extractor]
        J --> K[Metadata Parser]
    end
    
    subgraph "External Resources"
        L[Target Websites]
        M[Local Files]
        N[Raw Content]
    end
    
    subgraph "Output"
        O[CrawlResult]
        O --> O1[HTML Content]
        O --> O2[Markdown Text]
        O --> O3[Extracted Links]
        O --> O4[Media References]
        O --> O5[Status Information]
    end
    
    A --> F
    L --> A
    M --> A
    N --> A
    K --> O
    
    style A fill:#e3f2fd
    style B fill:#f3e5f5
    style F fill:#e8f5e8
    style O fill:#fff3e0
```

### Performance Comparison Flow

```mermaid
graph LR
    subgraph "HTTP Strategy Performance"
        A1[Request Start] --> A2[DNS Lookup: 50ms]
        A2 --> A3[TCP Connect: 100ms]
        A3 --> A4[HTTP Request: 200ms]
        A4 --> A5[Content Download: 300ms]
        A5 --> A6[Processing: 50ms]
        A6 --> A7[Total: ~700ms]
    end
    
    subgraph "Browser Strategy Performance"
        B1[Request Start] --> B2[Browser Launch: 2000ms]
        B2 --> B3[Page Navigation: 1000ms]
        B3 --> B4[JS Execution: 500ms]
        B4 --> B5[Content Rendering: 300ms]
        B5 --> B6[Processing: 100ms]
        B6 --> B7[Total: ~3900ms]
    end
    
    subgraph "Resource Usage"
        C1[HTTP Memory: ~50MB]
        C2[Browser Memory: ~500MB]
        C3[HTTP CPU: Low]
        C4[Browser CPU: High]
        C5[HTTP Concurrency: 100+]
        C6[Browser Concurrency: 10-20]
    end
    
    A7 --> D[5.5x Faster]
    B7 --> D
    C1 --> E[10x Less Memory]
    C2 --> E
    C5 --> F[5x More Concurrent]
    C6 --> F
    
    style A7 fill:#c8e6c9
    style B7 fill:#ffcdd2
    style C1 fill:#c8e6c9
    style C2 fill:#ffcdd2
    style C5 fill:#c8e6c9
    style C6 fill:#ffcdd2
```

### HTTP Request Types and Configuration

```mermaid
stateDiagram-v2
    [*] --> HTTPConfigSetup
    
    HTTPConfigSetup --> MethodSelection
    
    MethodSelection --> GET: Simple data retrieval
    MethodSelection --> POST: Form submission
    MethodSelection --> PUT: Data upload
    MethodSelection --> DELETE: Resource removal
    
    GET --> HeaderSetup: Set Accept headers
    POST --> PayloadSetup: JSON or form data
    PUT --> PayloadSetup: File or data upload
    DELETE --> AuthSetup: Authentication required
    
    PayloadSetup --> JSONPayload: application/json
    PayloadSetup --> FormPayload: form-data
    PayloadSetup --> RawPayload: custom content
    
    JSONPayload --> HeaderSetup
    FormPayload --> HeaderSetup
    RawPayload --> HeaderSetup
    
    HeaderSetup --> AuthSetup
    AuthSetup --> SSLSetup
    SSLSetup --> RedirectSetup
    RedirectSetup --> RequestExecution
    
    RequestExecution --> [*]: Request complete
    
    note right of GET : Default method for most crawling
    note right of POST : API interactions, form submissions
    note right of JSONPayload : Structured data transmission
    note right of HeaderSetup : User-Agent, Accept, Custom headers
```

### Error Handling and Retry Workflow

```mermaid
flowchart TD
    A[HTTP Request] --> B{Response Received?}
    
    B -->|No| C[Connection Error]
    B -->|Yes| D{Status Code Check}
    
    C --> C1{Timeout Error?}
    C1 -->|Yes| C2[ConnectionTimeoutError]
    C1 -->|No| C3[Network Error]
    
    D -->|2xx| E[Success Response]
    D -->|3xx| F[Redirect Response]
    D -->|4xx| G[Client Error]
    D -->|5xx| H[Server Error]
    
    F --> F1{Follow Redirects?}
    F1 -->|Yes| F2[Follow Redirect]
    F1 -->|No| F3[Return Redirect Response]
    F2 --> A
    
    G --> G1{Retry on 4xx?}
    G1 -->|No| G2[HTTPStatusError]
    G1 -->|Yes| I[Check Retry Count]
    
    H --> H1{Retry on 5xx?}
    H1 -->|Yes| I
    H1 -->|No| H2[HTTPStatusError]
    
    C2 --> I
    C3 --> I
    
    I --> J{Retries < Max?}
    J -->|No| K[Final Error]
    J -->|Yes| L[Calculate Backoff]
    
    L --> M[Wait Backoff Time]
    M --> N[Increment Retry Count]
    N --> A
    
    E --> O[Process Content]
    F3 --> O
    O --> P[Return CrawlResult]
    
    G2 --> Q[Error CrawlResult]
    H2 --> Q
    K --> Q
    
    style E fill:#c8e6c9
    style P fill:#c8e6c9
    style G2 fill:#ffcdd2
    style H2 fill:#ffcdd2
    style K fill:#ffcdd2
    style Q fill:#ffcdd2
```

### Batch Processing Architecture

```mermaid
sequenceDiagram
    participant Client
    participant BatchManager as Batch Manager
    participant HTTPPool as Connection Pool
    participant Workers as HTTP Workers
    participant Targets as Target Servers
    
    Client->>BatchManager: batch_crawl(urls)
    BatchManager->>BatchManager: create_semaphore(max_concurrent)
    
    loop For each URL batch
        BatchManager->>HTTPPool: acquire_connection()
        HTTPPool->>Workers: assign_worker()
        
        par Concurrent Processing
            Workers->>Targets: HTTP Request 1
            Workers->>Targets: HTTP Request 2
            Workers->>Targets: HTTP Request N
        end
        
        par Response Handling
            Targets-->>Workers: Response 1
            Targets-->>Workers: Response 2
            Targets-->>Workers: Response N
        end
        
        Workers->>HTTPPool: return_connection()
        HTTPPool->>BatchManager: batch_results()
    end
    
    BatchManager->>BatchManager: aggregate_results()
    BatchManager-->>Client: final_results()
    
    Note over Workers,Targets: 20-100 concurrent connections
    Note over BatchManager: Memory-efficient processing
    Note over HTTPPool: Connection reuse optimization
```

### Content Type Processing Pipeline

```mermaid
graph TD
    A[HTTP Response] --> B{Content-Type Detection}
    
    B -->|text/html| C[HTML Processing]
    B -->|application/json| D[JSON Processing]
    B -->|text/plain| E[Text Processing]
    B -->|application/xml| F[XML Processing]
    B -->|Other| G[Binary Processing]
    
    C --> C1[Parse HTML Structure]
    C1 --> C2[Extract Text Content]
    C2 --> C3[Generate Markdown]
    C3 --> C4[Extract Links/Media]
    
    D --> D1[Parse JSON Structure]
    D1 --> D2[Extract Data Fields]
    D2 --> D3[Format as Readable Text]
    
    E --> E1[Clean Text Content]
    E1 --> E2[Basic Formatting]
    
    F --> F1[Parse XML Structure]
    F1 --> F2[Extract Text Nodes]
    F2 --> F3[Convert to Markdown]
    
    G --> G1[Save Binary Content]
    G1 --> G2[Generate Metadata]
    
    C4 --> H[Content Analysis]
    D3 --> H
    E2 --> H
    F3 --> H
    G2 --> H
    
    H --> I[Link Extraction]
    H --> J[Media Detection]
    H --> K[Metadata Parsing]
    
    I --> L[CrawlResult Assembly]
    J --> L
    K --> L
    
    L --> M[Final Output]
    
    style C fill:#e8f5e8
    style H fill:#fff3e0
    style L fill:#e3f2fd
    style M fill:#c8e6c9
```

### Integration with Processing Strategies

```mermaid
graph LR
    subgraph "HTTP Strategy Core"
        A[HTTP Request] --> B[Raw Content]
        B --> C[Content Decoder]
    end
    
    subgraph "Processing Pipeline"
        C --> D[HTML Cleaner]
        D --> E[Markdown Generator]
        E --> F{Content Filter?}
        
        F -->|Yes| G[Pruning Filter]
        F -->|Yes| H[BM25 Filter]
        F -->|No| I[Raw Markdown]
        
        G --> J[Fit Markdown]
        H --> J
    end
    
    subgraph "Extraction Strategies"
        I --> K[CSS Extraction]
        J --> K
        I --> L[XPath Extraction]
        J --> L
        I --> M[LLM Extraction]
        J --> M
    end
    
    subgraph "Output Generation"
        K --> N[Structured JSON]
        L --> N
        M --> N
        
        I --> O[Clean Markdown]
        J --> P[Filtered Content]
        
        N --> Q[Final CrawlResult]
        O --> Q
        P --> Q
    end
    
    style A fill:#e3f2fd
    style C fill:#f3e5f5
    style E fill:#e8f5e8
    style Q fill:#c8e6c9
```

**📖 Learn more:** [HTTP vs Browser Strategies](https://docs.crawl4ai.com/core/browser-crawler-config/), [Performance Optimization](https://docs.crawl4ai.com/advanced/multi-url-crawling/), [Error Handling](https://docs.crawl4ai.com/api/async-webcrawler/)

---


## Advanced Filters & Scorers - Full Content
Component ID: deep_crawl_advanced_filters_scorers
Context Type: memory
Estimated tokens: 2,713

## Deep Crawling Filters & Scorers

Advanced URL filtering and scoring strategies for intelligent deep crawling with performance optimization.

### URL Filters - Content and Domain Control

```python
from crawl4ai.deep_crawling.filters import (
    URLPatternFilter, DomainFilter, ContentTypeFilter, 
    FilterChain, ContentRelevanceFilter, SEOFilter
)

# Pattern-based filtering
pattern_filter = URLPatternFilter(
    patterns=[
        "*.html",           # HTML pages only
        "*/blog/*",         # Blog posts
        "*/articles/*",     # Article pages
        "*2024*",          # Recent content
        "^https://example.com/docs/.*"  # Regex pattern
    ],
    use_glob=True,
    reverse=False  # False = include matching, True = exclude matching
)

# Domain filtering with subdomains
domain_filter = DomainFilter(
    allowed_domains=["example.com", "docs.example.com"],
    blocked_domains=["ads.example.com", "tracker.com"]
)

# Content type filtering
content_filter = ContentTypeFilter(
    allowed_types=["text/html", "application/pdf"],
    check_extension=True
)

# Apply individual filters
url = "https://example.com/blog/2024/article.html"
print(f"Pattern filter: {pattern_filter.apply(url)}")
print(f"Domain filter: {domain_filter.apply(url)}")
print(f"Content filter: {content_filter.apply(url)}")
```

### Filter Chaining - Combine Multiple Filters

```python
# Create filter chain for comprehensive filtering
filter_chain = FilterChain([
    DomainFilter(allowed_domains=["example.com"]),
    URLPatternFilter(patterns=["*/blog/*", "*/docs/*"]),
    ContentTypeFilter(allowed_types=["text/html"])
])

# Apply chain to URLs
urls = [
    "https://example.com/blog/post1.html",
    "https://spam.com/content.html",
    "https://example.com/blog/image.jpg",
    "https://example.com/docs/guide.html"
]

async def filter_urls(urls, filter_chain):
    filtered = []
    for url in urls:
        if await filter_chain.apply(url):
            filtered.append(url)
    return filtered

# Usage
filtered_urls = await filter_urls(urls, filter_chain)
print(f"Filtered URLs: {filtered_urls}")

# Check filter statistics
for filter_obj in filter_chain.filters:
    stats = filter_obj.stats
    print(f"{filter_obj.name}: {stats.passed_urls}/{stats.total_urls} passed")
```

### Advanced Content Filters

```python
# BM25-based content relevance filtering
relevance_filter = ContentRelevanceFilter(
    query="python machine learning tutorial",
    threshold=0.5,  # Minimum relevance score
    k1=1.2,        # TF saturation parameter
    b=0.75,        # Length normalization
    avgdl=1000     # Average document length
)

# SEO quality filtering
seo_filter = SEOFilter(
    threshold=0.65,  # Minimum SEO score
    keywords=["python", "tutorial", "guide"],
    weights={
        "title_length": 0.15,
        "title_kw": 0.18,
        "meta_description": 0.12,
        "canonical": 0.10,
        "robot_ok": 0.20,
        "schema_org": 0.10,
        "url_quality": 0.15
    }
)

# Apply advanced filters
url = "https://example.com/python-ml-tutorial"
relevance_score = await relevance_filter.apply(url)
seo_score = await seo_filter.apply(url)

print(f"Relevance: {relevance_score}, SEO: {seo_score}")
```

### URL Scorers - Quality and Relevance Scoring

```python
from crawl4ai.deep_crawling.scorers import (
    KeywordRelevanceScorer, PathDepthScorer, ContentTypeScorer,
    FreshnessScorer, DomainAuthorityScorer, CompositeScorer
)

# Keyword relevance scoring
keyword_scorer = KeywordRelevanceScorer(
    keywords=["python", "tutorial", "guide", "machine", "learning"],
    weight=1.0,
    case_sensitive=False
)

# Path depth scoring (optimal depth = 3)
depth_scorer = PathDepthScorer(
    optimal_depth=3,  # /category/subcategory/article
    weight=0.8
)

# Content type scoring
content_type_scorer = ContentTypeScorer(
    type_weights={
        "html": 1.0,    # Highest priority
        "pdf": 0.8,     # Medium priority
        "txt": 0.6,     # Lower priority
        "doc": 0.4      # Lowest priority
    },
    weight=0.9
)

# Freshness scoring
freshness_scorer = FreshnessScorer(
    weight=0.7,
    current_year=2024
)

# Domain authority scoring
domain_scorer = DomainAuthorityScorer(
    domain_weights={
        "python.org": 1.0,
        "github.com": 0.9,
        "stackoverflow.com": 0.85,
        "medium.com": 0.7,
        "personal-blog.com": 0.3
    },
    default_weight=0.5,
    weight=1.0
)

# Score individual URLs
url = "https://python.org/tutorial/2024/machine-learning.html"
scores = {
    "keyword": keyword_scorer.score(url),
    "depth": depth_scorer.score(url),
    "content": content_type_scorer.score(url),
    "freshness": freshness_scorer.score(url),
    "domain": domain_scorer.score(url)
}

print(f"Individual scores: {scores}")
```

### Composite Scoring - Combine Multiple Scorers

```python
# Create composite scorer combining all strategies
composite_scorer = CompositeScorer(
    scorers=[
        KeywordRelevanceScorer(["python", "tutorial"], weight=1.5),
        PathDepthScorer(optimal_depth=3, weight=1.0),
        ContentTypeScorer({"html": 1.0, "pdf": 0.8}, weight=1.2),
        FreshnessScorer(weight=0.8, current_year=2024),
        DomainAuthorityScorer({
            "python.org": 1.0,
            "github.com": 0.9
        }, weight=1.3)
    ],
    normalize=True  # Normalize by number of scorers
)

# Score multiple URLs
urls_to_score = [
    "https://python.org/tutorial/2024/basics.html",
    "https://github.com/user/python-guide/blob/main/README.md",
    "https://random-blog.com/old/2018/python-stuff.html",
    "https://python.org/docs/deep/nested/advanced/guide.html"
]

scored_urls = []
for url in urls_to_score:
    score = composite_scorer.score(url)
    scored_urls.append((url, score))

# Sort by score (highest first)
scored_urls.sort(key=lambda x: x[1], reverse=True)

for url, score in scored_urls:
    print(f"Score: {score:.3f} - {url}")

# Check scorer statistics
print(f"\nScoring statistics:")
print(f"URLs scored: {composite_scorer.stats._urls_scored}")
print(f"Average score: {composite_scorer.stats.get_average():.3f}")
```

### Advanced Filter Patterns

```python
# Complex pattern matching
advanced_patterns = URLPatternFilter(
    patterns=[
        r"^https://docs\.python\.org/\d+/",  # Python docs with version
        r".*/tutorial/.*\.html$",             # Tutorial pages
        r".*/guide/(?!deprecated).*",         # Guides but not deprecated
        "*/blog/{2020,2021,2022,2023,2024}/*", # Recent blog posts
        "**/{api,reference}/**/*.html"        # API/reference docs
    ],
    use_glob=True
)

# Exclude patterns (reverse=True)
exclude_filter = URLPatternFilter(
    patterns=[
        "*/admin/*",
        "*/login/*", 
        "*/private/*",
        "**/.*",          # Hidden files
        "*.{jpg,png,gif,css,js}$"  # Media and assets
    ],
    reverse=True  # Exclude matching patterns
)

# Content type with extension mapping
detailed_content_filter = ContentTypeFilter(
    allowed_types=["text", "application"],
    check_extension=True,
    ext_map={
        "html": "text/html",
        "htm": "text/html", 
        "md": "text/markdown",
        "pdf": "application/pdf",
        "doc": "application/msword",
        "docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    }
)
```

### Performance-Optimized Filtering

```python
# High-performance filter chain for large-scale crawling
class OptimizedFilterChain:
    def __init__(self):
        # Fast filters first (domain, patterns)
        self.fast_filters = [
            DomainFilter(
                allowed_domains=["example.com", "docs.example.com"],
                blocked_domains=["ads.example.com"]
            ),
            URLPatternFilter([
                "*.html", "*.pdf", "*/blog/*", "*/docs/*"
            ])
        ]
        
        # Slower filters last (content analysis)
        self.slow_filters = [
            ContentRelevanceFilter(
                query="important content",
                threshold=0.3
            )
        ]
    
    async def apply_optimized(self, url: str) -> bool:
        # Apply fast filters first
        for filter_obj in self.fast_filters:
            if not filter_obj.apply(url):
                return False
        
        # Only apply slow filters if fast filters pass
        for filter_obj in self.slow_filters:
            if not await filter_obj.apply(url):
                return False
        
        return True

# Batch filtering with concurrency
async def batch_filter_urls(urls, filter_chain, max_concurrent=50):
    import asyncio
    semaphore = asyncio.Semaphore(max_concurrent)
    
    async def filter_single(url):
        async with semaphore:
            return await filter_chain.apply(url), url
    
    tasks = [filter_single(url) for url in urls]
    results = await asyncio.gather(*tasks)
    
    return [url for passed, url in results if passed]

# Usage with 1000 URLs
large_url_list = [f"https://example.com/page{i}.html" for i in range(1000)]
optimized_chain = OptimizedFilterChain()
filtered = await batch_filter_urls(large_url_list, optimized_chain)
```

### Custom Filter Implementation

```python
from crawl4ai.deep_crawling.filters import URLFilter
import re

class CustomLanguageFilter(URLFilter):
    """Filter URLs by language indicators"""
    
    def __init__(self, allowed_languages=["en"], weight=1.0):
        super().__init__()
        self.allowed_languages = set(allowed_languages)
        self.lang_patterns = {
            "en": re.compile(r"/en/|/english/|lang=en"),
            "es": re.compile(r"/es/|/spanish/|lang=es"),
            "fr": re.compile(r"/fr/|/french/|lang=fr"),
            "de": re.compile(r"/de/|/german/|lang=de")
        }
    
    def apply(self, url: str) -> bool:
        # Default to English if no language indicators
        if not any(pattern.search(url) for pattern in self.lang_patterns.values()):
            result = "en" in self.allowed_languages
            self._update_stats(result)
            return result
        
        # Check for allowed languages
        for lang in self.allowed_languages:
            if lang in self.lang_patterns:
                if self.lang_patterns[lang].search(url):
                    self._update_stats(True)
                    return True
        
        self._update_stats(False)
        return False

# Custom scorer implementation
from crawl4ai.deep_crawling.scorers import URLScorer

class CustomComplexityScorer(URLScorer):
    """Score URLs by content complexity indicators"""
    
    def __init__(self, weight=1.0):
        super().__init__(weight)
        self.complexity_indicators = {
            "tutorial": 0.9,
            "guide": 0.8, 
            "example": 0.7,
            "reference": 0.6,
            "api": 0.5
        }
    
    def _calculate_score(self, url: str) -> float:
        url_lower = url.lower()
        max_score = 0.0
        
        for indicator, score in self.complexity_indicators.items():
            if indicator in url_lower:
                max_score = max(max_score, score)
        
        return max_score

# Use custom filters and scorers
custom_filter = CustomLanguageFilter(allowed_languages=["en", "es"])
custom_scorer = CustomComplexityScorer(weight=1.2)

url = "https://example.com/en/tutorial/advanced-guide.html"
passes_filter = custom_filter.apply(url)
complexity_score = custom_scorer.score(url)

print(f"Passes language filter: {passes_filter}")
print(f"Complexity score: {complexity_score}")
```

### Integration with Deep Crawling

```python
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai.deep_crawling import DeepCrawlStrategy

async def deep_crawl_with_filtering():
    # Create comprehensive filter chain
    filter_chain = FilterChain([
        DomainFilter(allowed_domains=["python.org"]),
        URLPatternFilter(["*/tutorial/*", "*/guide/*", "*/docs/*"]),
        ContentTypeFilter(["text/html"]),
        SEOFilter(threshold=0.6, keywords=["python", "programming"])
    ])
    
    # Create composite scorer
    scorer = CompositeScorer([
        KeywordRelevanceScorer(["python", "tutorial"], weight=1.5),
        FreshnessScorer(weight=0.8),
        PathDepthScorer(optimal_depth=3, weight=1.0)
    ], normalize=True)
    
    # Configure deep crawl strategy with filters and scorers
    deep_strategy = DeepCrawlStrategy(
        max_depth=3,
        max_pages=100,
        url_filter=filter_chain,
        url_scorer=scorer,
        score_threshold=0.6  # Only crawl URLs scoring above 0.6
    )
    
    config = CrawlerRunConfig(
        deep_crawl_strategy=deep_strategy,
        cache_mode=CacheMode.BYPASS
    )
    
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url="https://python.org",
            config=config
        )
        
        print(f"Deep crawl completed: {result.success}")
        if hasattr(result, 'deep_crawl_results'):
            print(f"Pages crawled: {len(result.deep_crawl_results)}")

# Run the deep crawl
await deep_crawl_with_filtering()
```

**📖 Learn more:** [Deep Crawling Strategy](https://docs.crawl4ai.com/core/deep-crawling/), [Custom Filter Development](https://docs.crawl4ai.com/advanced/custom-filters/), [Performance Optimization](https://docs.crawl4ai.com/advanced/performance-tuning/)

---


## Advanced Filters & Scorers - Diagrams & Workflows
Component ID: deep_crawl_advanced_filters_scorers
Context Type: reasoning
Estimated tokens: 3,030

## Deep Crawling Filters & Scorers Architecture

Visual representations of advanced URL filtering, scoring strategies, and performance optimization workflows for intelligent deep crawling.

### Filter Chain Processing Pipeline

```mermaid
flowchart TD
    A[URL Input] --> B{Domain Filter}
    B -->|✓ Pass| C{Pattern Filter}
    B -->|✗ Fail| X1[Reject: Invalid Domain]
    
    C -->|✓ Pass| D{Content Type Filter}
    C -->|✗ Fail| X2[Reject: Pattern Mismatch]
    
    D -->|✓ Pass| E{SEO Filter}
    D -->|✗ Fail| X3[Reject: Wrong Content Type]
    
    E -->|✓ Pass| F{Content Relevance Filter}
    E -->|✗ Fail| X4[Reject: Low SEO Score]
    
    F -->|✓ Pass| G[URL Accepted]
    F -->|✗ Fail| X5[Reject: Low Relevance]
    
    G --> H[Add to Crawl Queue]
    
    subgraph "Fast Filters"
        B
        C
        D
    end
    
    subgraph "Slow Filters"
        E
        F
    end
    
    style A fill:#e3f2fd
    style G fill:#c8e6c9
    style H fill:#e8f5e8
    style X1 fill:#ffcdd2
    style X2 fill:#ffcdd2
    style X3 fill:#ffcdd2
    style X4 fill:#ffcdd2
    style X5 fill:#ffcdd2
```

### URL Scoring System Architecture

```mermaid
graph TB
    subgraph "Input URL"
        A[https://python.org/tutorial/2024/ml-guide.html]
    end
    
    subgraph "Individual Scorers"
        B[Keyword Relevance Scorer]
        C[Path Depth Scorer]
        D[Content Type Scorer]
        E[Freshness Scorer]
        F[Domain Authority Scorer]
    end
    
    subgraph "Scoring Process"
        B --> B1[Keywords: python, tutorial, ml<br/>Score: 0.85]
        C --> C1[Depth: 4 levels<br/>Optimal: 3<br/>Score: 0.75]
        D --> D1[Content: HTML<br/>Score: 1.0]
        E --> E1[Year: 2024<br/>Score: 1.0]
        F --> F1[Domain: python.org<br/>Score: 1.0]
    end
    
    subgraph "Composite Scoring"
        G[Weighted Combination]
        B1 --> G
        C1 --> G
        D1 --> G
        E1 --> G
        F1 --> G
    end
    
    subgraph "Final Result"
        H[Composite Score: 0.92]
        I{Score > Threshold?}
        J[Accept URL]
        K[Reject URL]
    end
    
    A --> B
    A --> C
    A --> D
    A --> E
    A --> F
    
    G --> H
    H --> I
    I -->|✓ 0.92 > 0.6| J
    I -->|✗ Score too low| K
    
    style A fill:#e3f2fd
    style G fill:#fff3e0
    style H fill:#e8f5e8
    style J fill:#c8e6c9
    style K fill:#ffcdd2
```

### Filter vs Scorer Decision Matrix

```mermaid
flowchart TD
    A[URL Processing Decision] --> B{Binary Decision Needed?}
    
    B -->|Yes - Include/Exclude| C[Use Filters]
    B -->|No - Quality Rating| D[Use Scorers]
    
    C --> C1{Filter Type Needed?}
    C1 -->|Domain Control| C2[DomainFilter]
    C1 -->|Pattern Matching| C3[URLPatternFilter]
    C1 -->|Content Type| C4[ContentTypeFilter]
    C1 -->|SEO Quality| C5[SEOFilter]
    C1 -->|Content Relevance| C6[ContentRelevanceFilter]
    
    D --> D1{Scoring Criteria?}
    D1 -->|Keyword Relevance| D2[KeywordRelevanceScorer]
    D1 -->|URL Structure| D3[PathDepthScorer]
    D1 -->|Content Quality| D4[ContentTypeScorer]
    D1 -->|Time Sensitivity| D5[FreshnessScorer]
    D1 -->|Source Authority| D6[DomainAuthorityScorer]
    
    C2 --> E[Chain Filters]
    C3 --> E
    C4 --> E
    C5 --> E
    C6 --> E
    
    D2 --> F[Composite Scorer]
    D3 --> F
    D4 --> F
    D5 --> F
    D6 --> F
    
    E --> G[Binary Output: Pass/Fail]
    F --> H[Numeric Score: 0.0-1.0]
    
    G --> I[Apply to URL Queue]
    H --> J[Priority Ranking]
    
    style C fill:#e8f5e8
    style D fill:#fff3e0
    style E fill:#f3e5f5
    style F fill:#e3f2fd
    style G fill:#c8e6c9
    style H fill:#ffecb3
```

### Performance Optimization Strategy

```mermaid
sequenceDiagram
    participant Queue as URL Queue
    participant Fast as Fast Filters
    participant Slow as Slow Filters
    participant Score as Scorers
    participant Output as Filtered URLs
    
    Note over Queue, Output: Batch Processing (1000 URLs)
    
    Queue->>Fast: Apply Domain Filter
    Fast-->>Queue: 60% passed (600 URLs)
    
    Queue->>Fast: Apply Pattern Filter
    Fast-->>Queue: 70% passed (420 URLs)
    
    Queue->>Fast: Apply Content Type Filter
    Fast-->>Queue: 90% passed (378 URLs)
    
    Note over Fast: Fast filters eliminate 62% of URLs
    
    Queue->>Slow: Apply SEO Filter (378 URLs)
    Slow-->>Queue: 80% passed (302 URLs)
    
    Queue->>Slow: Apply Relevance Filter
    Slow-->>Queue: 75% passed (227 URLs)
    
    Note over Slow: Content analysis on remaining URLs
    
    Queue->>Score: Calculate Composite Scores
    Score-->>Queue: Scored and ranked
    
    Queue->>Output: Top 100 URLs by score
    Output-->>Queue: Processing complete
    
    Note over Queue, Output: Total: 90% filtered out, 10% high-quality URLs retained
```

### Custom Filter Implementation Flow

```mermaid
stateDiagram-v2
    [*] --> Planning
    
    Planning --> IdentifyNeeds: Define filtering criteria
    IdentifyNeeds --> ChooseType: Binary vs Scoring decision
    
    ChooseType --> FilterImpl: Binary decision needed
    ChooseType --> ScorerImpl: Quality rating needed
    
    FilterImpl --> InheritURLFilter: Extend URLFilter base class
    ScorerImpl --> InheritURLScorer: Extend URLScorer base class
    
    InheritURLFilter --> ImplementApply: def apply(url) -> bool
    InheritURLScorer --> ImplementScore: def _calculate_score(url) -> float
    
    ImplementApply --> AddLogic: Add custom filtering logic
    ImplementScore --> AddLogic
    
    AddLogic --> TestFilter: Unit testing
    TestFilter --> OptimizePerf: Performance optimization
    
    OptimizePerf --> Integration: Integrate with FilterChain
    Integration --> Production: Deploy to production
    
    Production --> Monitor: Monitor performance
    Monitor --> Tune: Tune parameters
    Tune --> Production
    
    note right of Planning : Consider performance impact
    note right of AddLogic : Handle edge cases
    note right of OptimizePerf : Cache frequently accessed data
```

### Filter Chain Optimization Patterns

```mermaid
graph TB
    subgraph "Naive Approach - Poor Performance"
        A1[All URLs] --> B1[Slow Filter 1]
        B1 --> C1[Slow Filter 2]
        C1 --> D1[Fast Filter 1]
        D1 --> E1[Fast Filter 2]
        E1 --> F1[Final Results]
        
        B1 -.->|High CPU| G1[Performance Issues]
        C1 -.->|Network Calls| G1
    end
    
    subgraph "Optimized Approach - High Performance"
        A2[All URLs] --> B2[Fast Filter 1]
        B2 --> C2[Fast Filter 2]
        C2 --> D2[Batch Process]
        D2 --> E2[Slow Filter 1]
        E2 --> F2[Slow Filter 2]
        F2 --> G2[Final Results]
        
        D2 --> H2[Concurrent Processing]
        H2 --> I2[Semaphore Control]
    end
    
    subgraph "Performance Metrics"
        J[Processing Time]
        K[Memory Usage]
        L[CPU Utilization]
        M[Network Requests]
    end
    
    G1 -.-> J
    G1 -.-> K
    G1 -.-> L
    G1 -.-> M
    
    G2 -.-> J
    G2 -.-> K
    G2 -.-> L
    G2 -.-> M
    
    style A1 fill:#ffcdd2
    style G1 fill:#ffcdd2
    style A2 fill:#c8e6c9
    style G2 fill:#c8e6c9
    style H2 fill:#e8f5e8
    style I2 fill:#e8f5e8
```

### Composite Scoring Weight Distribution

```mermaid
pie title Composite Scorer Weight Distribution
    "Keyword Relevance (30%)" : 30
    "Domain Authority (25%)" : 25
    "Content Type (20%)" : 20
    "Freshness (15%)" : 15
    "Path Depth (10%)" : 10
```

### Deep Crawl Integration Architecture

```mermaid
graph TD
    subgraph "Deep Crawl Strategy"
        A[Start URL] --> B[Extract Links]
        B --> C[Apply Filter Chain]
        C --> D[Calculate Scores]
        D --> E[Priority Queue]
        E --> F[Crawl Next URL]
        F --> B
    end
    
    subgraph "Filter Chain Components"
        C --> C1[Domain Filter]
        C --> C2[Pattern Filter]
        C --> C3[Content Filter]
        C --> C4[SEO Filter]
        C --> C5[Relevance Filter]
    end
    
    subgraph "Scoring Components"
        D --> D1[Keyword Scorer]
        D --> D2[Depth Scorer]
        D --> D3[Freshness Scorer]
        D --> D4[Authority Scorer]
        D --> D5[Composite Score]
    end
    
    subgraph "Queue Management"
        E --> E1{Score > Threshold?}
        E1 -->|Yes| E2[High Priority Queue]
        E1 -->|No| E3[Low Priority Queue]
        E2 --> F
        E3 --> G[Delayed Processing]
    end
    
    subgraph "Control Flow"
        H{Max Depth Reached?}
        I{Max Pages Reached?}
        J[Stop Crawling]
    end
    
    F --> H
    H -->|No| I
    H -->|Yes| J
    I -->|No| B
    I -->|Yes| J
    
    style A fill:#e3f2fd
    style E2 fill:#c8e6c9
    style E3 fill:#fff3e0
    style J fill:#ffcdd2
```

### Filter Performance Comparison

```mermaid
xychart-beta
    title "Filter Performance Comparison (1000 URLs)"
    x-axis [Domain, Pattern, ContentType, SEO, Relevance]
    y-axis "Processing Time (ms)" 0 --> 1000
    bar [50, 80, 45, 300, 800]
```

### Scoring Algorithm Workflow

```mermaid
flowchart TD
    A[Input URL] --> B[Parse URL Components]
    B --> C[Extract Features]
    
    C --> D[Domain Analysis]
    C --> E[Path Analysis] 
    C --> F[Content Type Detection]
    C --> G[Keyword Extraction]
    C --> H[Freshness Detection]
    
    D --> I[Domain Authority Score]
    E --> J[Path Depth Score]
    F --> K[Content Type Score]
    G --> L[Keyword Relevance Score]
    H --> M[Freshness Score]
    
    I --> N[Apply Weights]
    J --> N
    K --> N
    L --> N
    M --> N
    
    N --> O[Normalize Scores]
    O --> P[Calculate Final Score]
    P --> Q{Score >= Threshold?}
    
    Q -->|Yes| R[Accept for Crawling]
    Q -->|No| S[Reject URL]
    
    R --> T[Add to Priority Queue]
    S --> U[Log Rejection Reason]
    
    style A fill:#e3f2fd
    style P fill:#fff3e0
    style R fill:#c8e6c9
    style S fill:#ffcdd2
    style T fill:#e8f5e8
```

**📖 Learn more:** [Deep Crawling Strategy](https://docs.crawl4ai.com/core/deep-crawling/), [Performance Optimization](https://docs.crawl4ai.com/advanced/performance-tuning/), [Custom Implementations](https://docs.crawl4ai.com/advanced/custom-filters/)

---

