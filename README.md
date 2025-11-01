# Upwork Browser Connect Scraper

Jednostavan i efikasan Upwork scraper koji se povezuje sa postojećim Chrome browser-om.

## 🎯 Šta radi

- Povezuje se sa Chrome browser-om na portu 9222
- Koristi tvoju postojeću Upwork sesiju
- Zaobilazi Cloudflare zaštitu
- Scrape-uje job listing-e
- Čuva rezultate u HTML fajl
- **🤖 AI Cover Letter Generation**: Automatski generiše personalizovane cover letter-e za poslove koristeći OpenAI ili lokalne AI modele
- **💾 Database Integration**: Čuva sve podatke u SQLite bazi sa mogućnošću pretrage i analize
- **🖥️ Modern GUI**: Intuitivan tkinter interfejs sa tabovima za sve funkcionalnosti

## 🚀 Korišćenje

### 1. Pokreni Chrome sa debugging-om
```bash
# Koristi batch fajl:
start_chrome_debug.bat

# Ili ručno:
chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\temp\chrome-debug"
```

### 2. Uloguj se na Upwork
- Otvori https://www.upwork.com/
- Reši Cloudflare challenge ako se pojavi
- Uloguj se u svoj nalog

### 3. Pokreni scraper
```bash
# Iz root direktorijuma:
npm start

# Ili direktno:
node js_scrapers/browser_connect_puppeteer.js
```

## 📁 Struktura

```
upwork-notifier/
├── js_scrapers/
│   ├── browser_connect_puppeteer.js  # Glavni scraper
│   ├── package.json                  # Node.js dependencies
│   └── node_modules/                 # Instalirane biblioteke
├── start_chrome_debug.bat            # Batch za Chrome debug
├── package.json                      # Root package.json
└── README.md                         # Ova dokumentacija
```

## 🔧 Setup

### Instaliraj dependencies
```bash
npm install
```

### Verifikuj Chrome
Chrome mora biti pokrenut sa `--remote-debugging-port=9222` flag-om.

## 🎯 Kako funkcioniše

1. **Browser Connect**: Puppeteer se povezuje sa postojećim Chrome-om
2. **Session Reuse**: Koristi tvoju ulogovanu sesiju
3. **Cloudflare Bypass**: Zaobilazi detekciju jer izgleda kao normalan korisnik
4. **Job Scraping**: Preuzima HTML sa jobs stranice
5. **Data Export**: Čuva rezultate u HTML fajl

## 📊 Output

Scraper će kreirati HTML fajl: `browser_connect_YYYY-MM-DDTHH-mm-ss.html`

## 🛠️ Troubleshooting

### "Could not connect to Chrome"
- Proveri da li je Chrome pokrenut sa `--remote-debugging-port=9222`
- Zatvori sve Chrome prozore i pokreni ponovo

### Cloudflare još uvek blokira
- Uloguj se ručno u Chrome-u
- Reši challenge u browser-u pre pokretanja scrapera

### Nema poslova u rezultatu
- Proveri da li si na pravoj stranici u Chrome-u
- Idi na https://www.upwork.com/nx/jobs/search/?q=python

## ⚡ Prednosti ovog pristupa

- ✅ **Zaobilazi Cloudflare** - koristi stvarnu sesiju
- ✅ **Jednostavan** - samo Chrome + Node.js
- ✅ **Pouzdan** - nema bot detekciju
- ✅ **Brz setup** - nema kompleksnih konfiguracija

## 🔄 Sledeći koraci

Za notifikacije o novim poslovima, možeš dodati:
- Cron job za periodično pokretanje
- Email notifikacije
- Desktop notifikacije

---

**🎉 Uživaj u scraping-u bez Cloudflare problema!**

- `upwork_simple_scraper.py` - Glavni scraper script4. **Kreiraj Python Virtual Environment**:

- `run_simple_scraper.bat` - Batch fajl za pokretanje   ```powershell

- `venv/` - Python virtual environment   python -m venv venv

- `.vscode/settings.json` - VS Code konfiguracija za venv   # Aktivacija:

   venv\Scripts\Activate.ps1

## Output   ```

5. **Instaliraj Dependencies**:

Script će sačuvati HTML response u fajl: `upwork_response_YYYYMMDD_HHMMSS.html`   ```powershell
   # JavaScript dependencies
   npm install
   cd ai_orchestrator; npm install
   cd ..\frontend; npm install
   
   # Python dependencies (u aktiviranom venv-u)
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

## �️ Cloudflare Bypass

Glavni izazov sa Upwork scraping-om je **Cloudflare zaštita**. Naš sistem koristi **hibridni pristup**:

### 🔄 Workflow:
1. **Chrome Debug Mode** - browser ostaje otvoren za AI kontrolu
2. **Manual Login** - ti rešavaš Cloudflare i logujueš se
3. **AI Takeover** - AI koristi tvoju postojeću sesiju  
4. **Automated Scraping** - AI scrape-uje poslove bez Cloudflare problema

### 🚀 Quick Bypass:
```powershell
# Jedan click bypass proces
npm run bypass-cloudflare
```

### 💡 Zašto ovo funkcioniše:
- **Cloudflare blokira bot-ove**, ne browser sesije
- **Jednom kada prođeš**, sesija ostaje aktivna
- **AI koristi istu sesiju** - Cloudflare ne detektuje
- **Debug mode** omogućava AI kontrolu postojećeg browser-a

## �🔧 Konfiguracija

### 1. Pokretanje AI Servisa
```powershell
# Pokretanje Ollama servisa
ollama serve
```

### 2. Pokretanje Chrome u Debug Modu
```powershell
# Koristi desktop shortcut ili:
chrome.exe --remote-debugging-port=9222 --user-data-dir=chrome_debug
```

### 3. Cloudflare Bypass (VAŽNO!)
```powershell
# Poseban script za Cloudflare bypass
.\bypass-cloudflare.ps1

# Ili via npm
npm run bypass-cloudflare

# Ili uključeno u main start
python start.py  # Automatski uključuje bypass korak
```

**Cloudflare Workflow:**
1. 🌐 Script otvara Chrome u debug modu
2. 🔐 **TI** se logujueš u Upwork manualno  
3. 🛡️ **TI** rešavaš Cloudflare/CAPTCHA
4. ✅ **AI** preuzima kontrolu nakon toga

## 🎯 Korišćenje

### Quick Start (Preporučeno)
```powershell
# Interaktivni quick start
.\quick-start.ps1

# Ili direktno:
.\quick-start.ps1 -Setup    # Setup sistema
.\quick-start.ps1 -Test     # Integration test
.\quick-start.ps1 -Start    # Pokretanje sistema
```

### Aktiviranje Virtual Environment
```powershell
# Windows - brza aktivacija
.\activate.ps1

# Ili manuelno:
venv\Scripts\Activate.ps1
```

### NPM Script Commands
```powershell
# Sve u jednom
npm run setup           # Pokreće setup.ps1
npm run activate        # Aktivira venv
npm run test:integration # Test sa venv
npm run install:python  # Instalira Python deps
npm run clean           # Čisti node_modules
```

### Test Integracije
```powershell
# Test cele komunikacije (u aktiviranom venv-u)
python ai_orchestrator/test_integration.py
```

### Pokretanje Sistema
```powershell
# Kompletni sistem (u aktiviranom venv-u)
python start.py

# Ili samo frontend
cd frontend
npm run dev
```

### Direktno Korišćenje Python AI-ja
```powershell
# U PowerShell-u sa aktiviranim venv-om
python -c "
from ai_orchestrator.python.orchestrator import AIOrchestrator
import asyncio

async def main():
    orchestrator = AIOrchestrator()
    
    # Lista URL-ova poslova
    job_urls = [
        'https://www.upwork.com/jobs/~01234567890abcdef',
        'https://www.upwork.com/jobs/~02345678901bcdefg'
    ]
    
    # Kreiranje Excel fajla sa cover letter-ima
    excel_file = await orchestrator.process_job_batch(
        job_urls, 
        'John Doe',  # Ime
        ['Python', 'AI', 'Web Development']  # Veštine
    )
    print(f'Excel kreiran: {excel_file}')

asyncio.run(main())
"
```

### JavaScript Scraper
```powershell
# Direktno pokretanje
cd ai_orchestrator\js_scraper
node scraper_runner.js input_jobs.json
```

## 📊 Excel Output Format

Generisani Excel fajlovi su kompatibilni sa Monday.com:

| Column | Description |
|--------|-------------|
| Job Title | Naslov posla |
| Company | Ime kompanije |
| Budget | Budget posla |
| Description | Opis posla |
| Skills Required | Potrebne veštine |
| Cover Letter | AI generisan cover letter |
| Match Score | AI procena poklapanja (1-10) |
| Application Status | Status aplikacije |
| Job URL | Link ka poslu |
| Date Found | Datum pronaska |

## 🔍 Troubleshooting

### Chrome Debug Connection
```powershell
# Proveri da li je debug port otvoren
Invoke-WebRequest -Uri "http://localhost:9222/json/version"
```

### Ollama Service
```powershell
# Proveri status
ollama list

# Restartuj servis
ollama serve
```

### JavaScript Dependencies
```powershell
# Reinstaliraj dependencies
Remove-Item -Recurse -Force node_modules, package-lock.json
npm install
```

### Python Dependencies
```powershell
# Reinstaliraj Python dependencies
pip install --upgrade pip
pip install --force-reinstall -r requirements.txt

# Ili koristi npm script
npm run install:python
```

### Requirements.txt Objašnjenje
- **`requirements.txt`** - osnovni paketi potrebni za rad sistema
- **`requirements-dev.txt`** - dodatni dev tools (optional)

**Glavni requirements.txt sadrži**:
- **AI & HTTP**: aiohttp, requests za komunikaciju sa Qwen AI
- **Data Processing**: pandas, openpyxl za Excel generiranje  
- **Development**: pytest, flake8 za testiranje i code quality
- **Optional**: Komentarisani paketi za proširenja (OpenAI, Selenium, etc.)

**Development requirements (optional)**:
```powershell
# Za napredni development
pip install -r requirements-dev.txt
```

## 📁 Struktura Projekta

```
upwork-ai-automation/
├── 📁 ai_orchestrator/          # AI orchestration komponente
│   ├── 📁 python/               # Python AI servisi
│   │   ├── orchestrator.py      # Glavni orchestrator
│   │   ├── qwen_service.py      # Qwen AI servis
│   │   └── requirements.txt     # Python dependencies
│   ├── 📁 js_scraper/          # JavaScript scraper
│   │   ├── upworkScraper.js     # Glavni scraper
│   │   ├── scraper_runner.js    # Runner script
│   │   └── package.json         # JS dependencies
│   ├── 📁 output/              # Output fajlovi
│   ├── package.json            # AI orchestrator config
│   └── test_integration.py     # Integration tests
├── 📁 frontend/                # React frontend
│   ├── 📁 src/                 # Source kod
│   ├── 📁 public/              # Statički fajlovi
│   └── package.json            # Frontend dependencies
├── setup.ps1                   # Setup script
├── activate.ps1                # Venv activation
├── quick-start.ps1             # Interactive launcher
├── start.py                    # System launcher
├── package.json               # Root dependencies
└── README.md                  # Ova dokumentacija
```

## 🔄 Workflow

1. **Priprema**: Pokretanje Chrome debug, logovanje u Upwork
2. **Input**: Unos URL-ova poslova preko frontend-a
3. **Scraping**: JavaScript scraper preuzima podatke
4. **AI Analiza**: Python orchestrator analizira poslove
5. **Cover Letters**: AI generiše personalizovane cover letter-e
6. **Export**: Kreiranje Excel fajla za Monday.com
7. **Review**: Pregled i aplikiranje preko frontend-a

## ⚙️ Napredne Opcije

### Custom AI Prompts
```powershell
# Prilagođeni prompt za analizu
python -c "
from ai_orchestrator.python.orchestrator import AIOrchestrator
orchestrator = AIOrchestrator()
orchestrator.set_analysis_prompt('''
Analiziraj ovaj posao fokusirajući se na:
1. Tehničke zahteve
2. Budget vs scope
3. Klijentov profil
''')
"
```

### Batch Processing
```powershell
# Procesiranje velikih grupa poslova
python -c "
from ai_orchestrator.python.orchestrator import AIOrchestrator
import asyncio

async def process_batches():
    orchestrator = AIOrchestrator()
    job_url_batches = [['url1', 'url2'], ['url3', 'url4']]
    
    for batch in job_url_batches:
        results = await orchestrator.process_job_batch(batch)
        print(f'Batch processed: {len(results)} jobs')

asyncio.run(process_batches())
"
```

### Custom Selectors
```powershell
# Prilagođeni selektori za scraping
node -e "
const { UpworkJobScraper } = require('./ai_orchestrator/js_scraper/upworkScraper');

const customSelectors = {
    jobTitle: ['.job-title-custom', '.alternative-title'],
    description: ['.job-description-custom']
};

const scraper = new UpworkJobScraper();
scraper.updateSelectors(customSelectors);
"
```

## 🤝 Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open Pull Request

## 📝 License

MIT License - pogledaj [LICENSE](LICENSE) fajl za detalje.

## 🆘 Support

- **Issues**: [GitHub Issues](../../issues)
- **Dokumentacija**: [Wiki](../../wiki)
- **Email**: support@upwork-automation.com

## 🤖 AI Cover Letter Generation

Najnovija funkcija koja koristi veštačku inteligenciju za automatsko generisanje personalizovanih cover letter-a.

### 🔥 Features

- **Multi-Provider AI**: Podrška za OpenAI GPT i lokalne AI modele
- **Smart Job Analysis**: Analizira job requirements i generiše relevantne cover letter-e
- **Database Integration**: Automatsko čuvanje svih generisanih cover letter-a
- **GUI Integration**: Jednostavan interfejs u modernom GUI-ju
- **Batch Processing**: Mogućnost generisanja za više poslova odjednom
- **🤖 Custom Model Training**: Fine-tuning GPT-2 modela na vašim podacima za personalizovanije cover letter-e

### 🚀 Korišćenje

1. **Pokreni GUI**:
   ```bash
   python upwork_gui_modern.py
   ```

2. **Otvori AI Tab**:
   - Klikni na "🤖 AI Cover Letters" tab

3. **Izaberi Job**:
   - Klikni "🔍 Select Job" da izabereš posao iz baze

4. **Generiši Cover Letter**:
   - Klikni "🤖 Generate Letter" za AI generisanje

5. **Sačuvaj i Koristi**:
   - "💾 Save Letter" - sačuvaj u bazu
   - "📋 Copy Letter" - kopiraj u clipboard

### ⚙️ Setup

**OpenAI Setup**:
```bash
export OPENAI_API_KEY="your-api-key-here"
```

**Lokalni AI**:
- Konfiguriši putanju do modela u `ai/local_ai/config.json`

### 🧠 Custom Model Training

Sistem podržava trening custom GPT-2 modela za još personalizovanije cover letter-e:

#### Pokretanje Training-a:
```bash
# Aktiviraj virtual environment
venv\Scripts\Activate.ps1

# Pokreni training script
python ai/training/examples/train_advanced.py
```

#### Šta se trenira:
- **Dataset**: Koristi podatke iz `ai/training_data.json`
- **Model**: GPT-2 medium (355M parametara)
- **Training**: 5 epoha, optimizovano za CPU
- **Output**: Model se čuva u `trained_models/advanced_cover_letter_model/final/`

#### Rezultati:
- Model se automatski integriše u LocalAIProvider
- Cover letter-i postaju personalizovaniji
- Bolje razumevanje job requirements-a

#### Requirements za Training:
```bash
pip install transformers torch datasets accelerate
```

### 📚 Dokumentacija

Detaljna dokumentacija: [AI_COVER_LETTER_README.md](./AI_COVER_LETTER_README.md)

## 🎯 Roadmap

- [ ] **v1.1**: Multi-platform support (LinkedIn, Freelancer)
- [ ] **v1.2**: Advanced AI filtering
- [ ] **v1.3**: Automatic application submission
- [ ] **v1.4**: Performance analytics dashboard
- [ ] **v1.5**: Mobile app

---

**⚡ Happy Automating! ⚡**

*Razvijeno za efikasniju pretragu i aplikiranje na Upwork poslove.*