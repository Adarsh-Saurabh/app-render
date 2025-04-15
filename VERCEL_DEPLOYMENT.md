# Deploying to Vercel

This guide will help you deploy the Sign Language Detection application to Vercel.

## Prerequisites

1. A Vercel account (sign up at [vercel.com](https://vercel.com))
2. Git installed on your computer
3. Node.js and npm installed (for Vercel CLI)

## Deployment Steps

### Option 1: Using Vercel CLI

1. Install the Vercel CLI:
```bash
npm install -g vercel
```

2. Login to Vercel:
```bash
vercel login
```

3. Navigate to your project directory and deploy:
```bash
vercel
```

4. Follow the prompts to complete the deployment.

### Option 2: Using Vercel Dashboard

1. Push your code to a Git repository (GitHub, GitLab, or Bitbucket).

2. Go to [vercel.com/new](https://vercel.com/new) and import your repository.

3. Configure the project:
   - Framework Preset: Other
   - Build Command: `pip install -r requirements.txt`
   - Output Directory: `.`
   - Install Command: `pip install -r requirements.txt`

4. Click "Deploy" and wait for the deployment to complete.

## Important Notes

1. **Model File**: Make sure the `model.p` file is included in your repository. Vercel has a file size limit, so if your model is very large, you might need to host it elsewhere and download it during deployment.

2. **Environment Variables**: If you need to set environment variables, you can do so in the Vercel dashboard under the "Settings" tab.

3. **Serverless Limitations**: Vercel's serverless functions have execution time limits (typically 10 seconds for hobby plans). Our application is designed to work within these limits by processing frames on the client side and sending them to the server for classification.

4. **Cold Starts**: Serverless functions may experience "cold starts" when they haven't been used for a while. This can cause the first request to be slower.

## Troubleshooting

1. **Deployment Failures**: Check the deployment logs in the Vercel dashboard for errors.

2. **Model Loading Issues**: If the model fails to load, check that the file path is correct and the file is included in the deployment.

3. **API Errors**: If you see API errors in the browser console, check that the API endpoint URL is correct.

4. **Performance Issues**: If the application is slow, try reducing the frequency of frame processing in the JavaScript code.

## Testing Your Deployment

1. Visit your Vercel deployment URL (e.g., `https://your-app.vercel.app`).

2. Allow camera access when prompted.

3. Make sign language gestures in front of the camera.

4. The application should display the detected sign and confidence score. 