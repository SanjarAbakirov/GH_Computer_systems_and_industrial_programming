# PATH="./GH_Computer_systems_and_industrial_programming-main"
# cd "$PATH" || exit


echo "Control all changes in $PATH..."

while true; do
    if ! git diff --quiet || ! git diff --cached --quiet; then
		echo "Changes defined! Commit and push..."
		git add .
		git commit -m "auto commit $(date)" || true
		git push
    fi
    sleep 5
done

