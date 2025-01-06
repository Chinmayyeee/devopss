print("hi")
print("git init
git add hi.py 
git commit -m  "Initial Commit"
git branch
git remote add origin https://github.com/username/<repository-name>.git
git push -u origin master")
print("FROM python:3.9
COPY hi.py .
CMD ["python","hi.py"]
docker build -t hi.py
docker run hi.py")