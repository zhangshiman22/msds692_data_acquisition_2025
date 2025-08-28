git checkout feature/search
echo "# Example 1" > ex01.txt
git add ex01.txt
git commit -m "added ex01.txt"
git log --graph --all
git checkout main
echo "hello" > temp.txt
git add temp.txt
git commit -m "updated contents on the main branch"
git log --graph --all