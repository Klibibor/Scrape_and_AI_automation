# AI Cover Letter Generation Feature

This feature provides AI-powered cover letter generation for Upwork jobs using multiple AI providers.

## Features

- **Multi-Provider Support**: Supports both OpenAI GPT and local AI models
- **Database Integration**: Automatically saves generated cover letters to the database
- **GUI Integration**: Full integration with the modern Upwork GUI
- **Job Selection**: Easy job selection from existing database entries
- **Cover Letter Management**: View, edit, copy, and manage all generated cover letters

## Project Structure

```
ai/
├── __init__.py                 # Main AI module
├── cover_letter_generator.py   # Main generator class
├── local_ai/                   # Local AI provider
│   ├── __init__.py            # Local AI implementation
│   └── config.json            # Local AI configuration
└── openai/                     # OpenAI provider
    ├── __init__.py            # OpenAI implementation
    └── config.json            # OpenAI configuration
```

## Setup

### 1. Dependencies

Install required packages:

```bash
pip install openai  # For OpenAI provider
```

### 2. Configuration

#### OpenAI Setup
- Set your OpenAI API key as an environment variable:
  ```bash
  export OPENAI_API_KEY="your-api-key-here"
  ```
- Or modify `ai/openai/config.json` with your API key

#### Local AI Setup
- Configure your local AI model path in `ai/local_ai/config.json`
- Currently supports template-based generation (expandable for actual models)

### 3. Database

The feature automatically creates the `cover_letters` table when first run:

```sql
CREATE TABLE IF NOT EXISTS cover_letters (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_id INTEGER NOT NULL,
    ai_provider TEXT NOT NULL,
    cover_letter_text TEXT NOT NULL,
    generated_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    status TEXT DEFAULT 'generated',
    rating INTEGER,
    notes TEXT,
    FOREIGN KEY (job_id) REFERENCES jobs (id) ON DELETE CASCADE
);
```

## Usage

### GUI Usage

1. **Launch the Application**:
   ```bash
   python upwork_gui_modern.py
   ```

2. **Navigate to AI Tab**:
   - Click on the "🤖 AI Cover Letters" tab

3. **Select AI Provider**:
   - Choose between "openai" or "local_ai" from the dropdown

4. **Select a Job**:
   - Click "🔍 Select Job" to choose from available jobs in database

5. **Generate Cover Letter**:
   - Click "🤖 Generate Letter" to create AI-powered cover letter

6. **Save & Manage**:
   - Click "💾 Save Letter" to store in database
   - Click "📋 Copy Letter" to copy to clipboard
   - Click "📚 View All Letters" to browse all generated letters

### Programmatic Usage

```python
from ai.cover_letter_generator import CoverLetterGenerator
from data.database_manager import UpworkDatabase

# Initialize
generator = CoverLetterGenerator(preferred_provider='openai')
db = UpworkDatabase()

# Generate cover letter
job_data = {
    'title': 'Python Developer',
    'company': 'Tech Corp',
    'description': 'Looking for Python developer...',
    'skills': ['Python', 'Django', 'PostgreSQL']
}

cover_letter = generator.generate_cover_letter(job_data)
print(cover_letter)

# Save to database
job_id = 1  # From your jobs table
cover_letter_id = db.add_cover_letter(
    job_id=job_id,
    ai_provider='openai',
    cover_letter_text=cover_letter
)
```

## API Reference

### CoverLetterGenerator

Main class for cover letter generation.

#### Methods

- `__init__(preferred_provider='openai')`: Initialize with preferred provider
- `generate_cover_letter(job_data, provider=None)`: Generate cover letter
- `get_available_providers()`: Get list of available providers
- `set_preferred_provider(provider)`: Change preferred provider

### Database Methods

- `add_cover_letter(job_id, ai_provider, cover_letter_text, notes=None)`: Save cover letter
- `get_cover_letters_for_job(job_id)`: Get cover letters for specific job
- `get_recent_cover_letters(limit=20)`: Get recent cover letters
- `update_cover_letter_status(cover_letter_id, status, rating=None, notes=None)`: Update status
- `delete_cover_letter(cover_letter_id)`: Delete cover letter

## Testing

Run the test suite:

```bash
python test_ai_cover_letter.py
```

## Configuration Files

### ai/openai/config.json
```json
{
  "model": "gpt-3.5-turbo",
  "max_tokens": 1000,
  "temperature": 0.7,
  "system_prompt": "You are a professional cover letter writer..."
}
```

### ai/local_ai/config.json
```json
{
  "model_path": "models/local_ai_model",
  "max_tokens": 1000,
  "temperature": 0.7,
  "fallback_templates": [
    "I am excited to apply for the {job_title} position..."
  ]
}
```

## Troubleshooting

### Common Issues

1. **OpenAI API Key Not Set**:
   - Error: "OpenAI API key not provided"
   - Solution: Set `OPENAI_API_KEY` environment variable

2. **No Jobs in Database**:
   - Error: "No jobs found in database"
   - Solution: Run scraping first to populate jobs table

3. **Local AI Not Available**:
   - Error: "Local AI provider not available"
   - Solution: Configure local model path or use OpenAI

### Logs

Check the GUI console output for detailed error messages and status updates.

## Future Enhancements

- Support for more AI providers (Claude, Gemini, etc.)
- Custom prompt templates
- Cover letter editing and improvement suggestions
- Batch generation for multiple jobs
- Export cover letters to PDF/docx formats
- Integration with job application workflows

## Contributing

1. Follow existing code patterns
2. Add tests for new features
3. Update documentation
4. Test with both OpenAI and local providers</content>
<parameter name="filePath">e:\Repoi\UpworkNotif\AI_COVER_LETTER_README.md