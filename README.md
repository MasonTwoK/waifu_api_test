# ![](https://docs.waifu.im/~gitbook/image?url=https%3A%2F%2F1092558500-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FEOup5T74lqSrRXj6Bgtv%252Ficon%252FOfffK0V32Jh9Y2zXBTCO%252Ffavicon.png%3Falt%3Dmedia%26token%3Db61b819a-fb5c-4797-bec8-44faee2134a0&width=32&dpr=2&quality=100&sign=6e287f34&sv=2) BackEnd API tests for [Waifu.im](https://www.waifu.im/) by using Python & Pytest
Main idea of this project is to obtain solid understanding of next topics:
* 💻 BackEnd API testing
* 🤖 Test Automation with Python programing language & pyTest framework
* 🎨 Design Patterns in Automation Frameworks

## Project Structure
`tests/` - folder that contains all tests of the project in which assertions apply

`conftest.py` - contains methods & arrangements required for API request

`data.py` - contains pre-defined names, tags & data sets for arranging or applying assertions

`utils.py` - contains set of methods that processing response data (act) & allow to compare it with expected values

`requirements.txt` - contains names of libraries which is needed to be imported

`pytest.ini` - contains pytest markers

`Dockerfile` - that allows to assemble an image

## ▶️Getting Started

### Prerequisites

- Python 3.10+
- `pip` for dependency management

### Installation

```bash
git clone https://github.com/MasonTwoK/waifu_api_test.git
cd waifu_api_test
python -m venv env
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirments.txt
```
### To apply test launch 🚀 use next command:
```commandline
pytest . -v
```

## Environments
- Some API calls require authorization token `AUTH_TOKEN` to be applied. To get it please follow this [Guide of Generating a Token](https://docs.waifu.im/authentication#generating-a-token).
- Guide of getting [Discord ID](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID#h_01HRSTXPS5H5D7JBY2QKKPVKNA)

### To setup environment 
1. Create file `.env` in project folder
2. Add generated `AUTH_TOKEN` & `DISCORD_ID`
3. File should have similar structure:
```python
AUTH_TOKEN=xxxxxxxxxxxxxxxxxx
DISCORD_ID=xxxxxxxxxxxxxxxxxx
```
### ⚠️403 errors caused by [Cloudflare GeoBlocking](http://docs.waifu.im/cloudflare-geoblocking)
To avoid such issues please use VPN connection (preferably Germany)

## 🔧 Tech Stack
- Python
- Pytest
- Docker

### 📄 License
This project is open-source and available under the MIT License.
