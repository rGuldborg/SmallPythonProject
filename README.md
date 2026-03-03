# Currency CLI

Simpelt Python-CLI til valutaomregning med ExchangeRate API.

## Hent projektet
```bash
git clone <DIT_GITHUB_LINK>
cd currency-cli
```

## Opret virtual environment
### Windows (PowerShell)
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

## Installer pakker
```bash
pip install -r requirements.txt
```

## Kør programmet
Første gang (gemmer API key i `.env`):
```bash
python src/main.py --key DIN_API_KEY --from_currency USD --to_currency DKK --amount 100
```

Efterfølgende gange:
```bash
python src/main.py --from_currency USD --to_currency DKK --amount 100
```
