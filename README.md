# AI Outline CLI(Command-Line Interface)

An AI command-line tool that generates outlines for user defined topics and saves them as a Markdown files.
Supports Ollama and OpenAi.

## Setup:

### ***1. Clone the repo***
```bash
git clone <repo-url>
cd week3_cli
```
### ***2. Create a .env file***
```env
OLLAMA_API_KEY=local-test-key
```
OR
```env
OPENAI_API_KEY=your-personal-key
```
### ***3. Install dependencies***
```bash
pip install -r requirements.txt
```
### ***4. Run the CLI***
```bash
python outline_cli.py "(USER-DEFINED-TOPIC)"
```
## Example Run:
```bash
python outline_cli.py "Football" --bullets 3
```
### Creates
```bash
outlines/football.md
```
```markdown
# Football

- Team structure and roles
- Basic rules of the game
- Major tournaments
```
## AI vs Manual Code Segments
### Manual (written by me)
- `argparse` CLI setup
- `slugify()` function for safe filenames
- Git setup, .gitignore, README
- File creation logic

### AI-assisted
- Prompt design for bullet generation
- Chat completion call (OpenAI & Ollama usage)
- Markdown formatting tips
- Error handling suggestions
