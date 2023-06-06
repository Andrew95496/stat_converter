# script to create path for file saves
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

if [ ! -d "(pwd)/athletes/" ]; then
    rm /Users/drewskikatana/Documents/Programming/jiu_jistics/logger/* #! NOTE: DEPRECIATE AFTER DEPLOYMENT FOR TEST ONLY
    mkdir "$(pwd)/athletes/"
    mkdir "$(pwd)/logger/"
    echo -e "${YELLOW}Files will save at $(pwd)/athletes/${NC}"
fi
