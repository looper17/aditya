#!/bin/bash
echo "Pushing to GitHub repository: https://github.com/looper17/aditya.git"
echo ""
echo "You'll be prompted for your GitHub credentials:"
echo "  Username: looper17"
echo "  Password: Use a Personal Access Token (NOT your GitHub password)"
echo ""
echo "To create a token: https://github.com/settings/tokens/new"
echo "  - Select 'repo' scope"
echo "  - Copy the token and paste it as the password"
echo ""
git push -u origin main
