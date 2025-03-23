# Getting a Hugging Face Token for Llama 3.2

Here's how to get a Hugging Face token for accessing Llama 3.2 and set it as an environment variable:

## Step 1: Create a Hugging Face Account

1. Go to https://huggingface.co/
2. Click "Sign Up" in the top right corner
3. Complete the registration process

## Step 2: Create an Access Token

1. Log in to your Hugging Face account
2. Click on your profile picture in the top right
3. Select "Settings" from the dropdown menu
4. In the left sidebar, click on "Access Tokens"
5. Click "New Token"
6. Name your token (e.g., "Llama3-access")
7. Select appropriate permissions (at least "read" access)
8. Click "Generate Token"
9. **Important:** Copy your token - this is the only time you'll see it!

## Step 3: Accept the Llama 3 Model License

1. Go to Meta AI's model page: https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct
2. Click "Access repository"
3. Read and accept the license agreement

## Step 4: Set the Environment Variable

### On Windows (PowerShell):
```powershell
$env:HUGGING_FACE_HUB_TOKEN = "your_token_here"
```

### On Windows (Command Prompt):
```cmd
set HUGGING_FACE_HUB_TOKEN=your_token_here
```

### On macOS/Linux:
```bash
export HUGGING_FACE_HUB_TOKEN="your_token_here"
```