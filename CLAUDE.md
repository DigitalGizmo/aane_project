# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

Keep your replies concise and focus on conveying the key infomration. No unnecessary fluff, no long code snippets.

## Project Overview

The African Americans of the North East (AANE) project is a Django 4.2 application that serves as a historical database tracking enslaved African Americans and enslavers in the Northeast United States. The application manages primary historical sources, source entries, biographical information, and relationships between people.

## Development Commands

### Environment Setup
```bash
# Activate virtual environment
source .env-aane/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Database
```bash
# Run migrations
python manage.py migrate

# Create migrations after model changes
python manage.py makemigrations

# Access database shell
python manage.py dbshell
```

### Running the Development Server
```bash
# Default settings (uses config.settings.base)
python manage.py runserver

# With specific settings module
python manage.py runserver --settings=config.settings.local
```

### Django Admin
```bash
# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic
```

### Testing
```bash
# Run all tests
python manage.py test

# Run tests for specific app
python manage.py test apps.people
python manage.py test apps.sources
```

### Production Deployment
The application is configured to run with Gunicorn. Configuration is in [gunicorn.conf.py](gunicorn.conf.py):
```bash
gunicorn config.wsgi:application -c gunicorn.conf.py
```

## Architecture

### Settings Configuration
Settings are split across multiple files in [config/settings/](config/settings/):
- [base.py](config/settings/base.py) - Shared configuration for all environments
- `local.py` - Local development settings
- `remote_db.py` - Remote database configuration
- `staging.py` - Staging environment settings
- `secrets.json` - Credentials and secrets (not in version control)

The default settings module is `config.settings.base` (see [manage.py:6](manage.py#L6)).

### Application Structure
The project follows Django's reusable app pattern with apps in the [apps/](apps/) directory:

- **people** - Manages biographical information for African Americans (`AAPerson`) and others/enslavers (`OPerson`)
- **sources** - Handles primary/secondary sources, volumes, and individual source entries
- **locations** - Geographic data (towns and states)
- **about** - Static informational pages
- **sitewide** - Shared models and utilities (e.g., `CommonEditHistory` for edit tracking)

### Core Data Models

#### People App ([apps/people/models.py](apps/people/models.py))
- `PersonModel` (abstract) - Base model with fields common to both AAPerson and OPerson
- `AAPerson` - Enslaved and free African Americans
  - Fields: name, birth/death years, freed status, confidence level, tier
  - Relationships: Many-to-many with `OPerson` (enslavers), `SourceEntry` (through `aa_persons`), and `Town` (locations)
- `OPerson` - Enslavers, service providers, and other historical figures
  - Fields: name, role, race, title
  - Relationship: Many-to-many with `AAPerson`

#### Sources App ([apps/sources/models.py](apps/sources/models.py))
- `PrimarySource` - Historical documents (wills, deeds, church records, etc.)
  - Fields: title, source type, classification (primary/secondary), location, date range
- `Volume` - Volumes or subsections within a primary source
  - Relationship: Foreign key to `PrimarySource`
  - Fields: title, date range, accession numbers
- `SourceEntry` - Individual entries extracted from volumes
  - Fields: entry text (plain and HTML via TinyMCE), dates, monetary values, image references
  - Relationships: Foreign key to `Volume`, many-to-many with `AAPerson`, foreign key to `OPerson` (enslaver)
  - Important: Uses `entry_text_html` (TinyMCE field) for formatted display

#### Key Relationships
1. `SourceEntry` → `Volume` → `PrimarySource` (hierarchical source organization)
2. `SourceEntry` ↔ `AAPerson` (many-to-many through `aa_persons` field)
3. `SourceEntry` → `OPerson` (foreign key `operson_fk`)
4. `AAPerson` ↔ `OPerson` (many-to-many through `owners` field)
5. Both person types ↔ `Town` (many-to-many for locations)

### Frontend Architecture
- **Templates**: Django templates in [templates/](templates/) directory with app-specific subdirectories
- **HTMX**: Used for dynamic page updates without full page reloads
- **TinyMCE**: Rich text editor for biographical text and source entries
- **Static Files**: CSS/JS in [local_static/](local_static/)
- **Template Structure**: Base template is [base.html](templates/base.html), extended by app templates

### URL Structure
Main URL configuration in [config/urls.py](config/urls.py):
- `/` - Home page
- `/team/` - Team page
- `/sources/` - Sources app (includes volumes and entries)
- `/people/` - People app (AAPerson and OPerson views)
- `/about/` - About pages
- `/admin/` - Django admin interface
- `/api-auth/` - Django REST Framework authentication

### REST API
Django REST Framework is configured for API endpoints. See [apps/sources/serializers.py](apps/sources/serializers.py) and [apps/people/serializers.py](apps/people/serializers.py) for available serializers.

## Database Configuration
- **Engine**: PostgreSQL (psycopg2)
- **Database Name**: `aanedata`
- **User**: `aanedata_user`
- **Password**: Stored in `config/settings/secrets.json` as `DB_PASS`
- **Host**: 127.0.0.1
- **Port**: 5432

## Important Model Properties and Methods

### SourceEntry
- `safe_entry_html` - Returns HTML content with outer `<p>` tags stripped
- `truncated_entry_html` - Returns truncated HTML (72 chars default) for list displays
- `get_truncated_html(length)` - Method version allowing custom truncation length
- `aa_person` - Property to get related AAPerson via `aa_id`
- `o_person` - Property to get related OPerson via `operson_fk_id`

### AAPerson
- `person_entries_count` - Count of related source entries
- `person_url` - Public URL for the person's page

### Volume
- `active_entries` - Queryset of entries with `data_status >= 0`
- Date properties: `two_digit_month_start`, `two_digit_day_start`, etc.

## Static Files
- **STATIC_ROOT**: `../aane_static` (one directory above BASE_DIR)
- **STATIC_URL**: `/static/`
- **STATICFILES_DIRS**: `local_static/` within the project

## Key Conventions
1. **Apps in Python Path**: The [apps/](apps/) directory is added to `sys.path` in [base.py:13](config/settings/base.py#L13), so imports use `people.models` not `apps.people.models`
2. **Title Alpha**: Sources use `title_alpha` field for alphabetical sorting (handles articles like "The")
3. **Data Status**: SourceEntry uses `data_status` to track entry lifecycle (-2=delete, -1=inactive, 0=original, 1=new, 2=updated, 3=vetted)
4. **Research Status**: Both person types have `research_status` field (0=delete, 1=inactive, 2=needs research, 3=in progress, 6=publishable)

## Common Pitfalls
- **TinyMCE HTML Fields**: When working with `entry_text_html` or `bio_html` fields, be aware they wrap content in `<p>` tags. Use the `safe_entry_html` property for display.
- **Legacy IDs**: Multiple legacy ID fields exist (`aa_id`, `legacy_id`, `operson_id`) from data migration - use foreign key relationships (`operson_fk`, `aa_persons`) for new code.
- **Entry-Source Relationship**: SourceEntry connects to PrimarySource through Volume, not directly. Always use `entry.volume.primary_source`.
- **Secrets File**: The `secrets.json` file must exist with `SECRET_KEY` and `DB_PASS` keys for the application to run.
