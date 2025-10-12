# BackEnd API tests for [Waifu.im](https://www.waifu.im/) ![](https://docs.waifu.im/~gitbook/image?url=https%3A%2F%2F1092558500-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FEOup5T74lqSrRXj6Bgtv%252Ficon%252FOfffK0V32Jh9Y2zXBTCO%252Ffavicon.png%3Falt%3Dmedia%26token%3Db61b819a-fb5c-4797-bec8-44faee2134a0&width=32&dpr=2&quality=100&sign=6e287f34&sv=2) by using Python & Pytest
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

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- `pip` for dependency management

### Installation

```bash
git clone https://github.com/MasonTwoK/waifu_api_test.git
cd waifu_api_test
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirments.txt
```

## 🔧 Tech Stack
- Python
- Pytest

### 📄 License
This project is open-source and available under the MIT License.
