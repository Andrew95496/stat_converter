# script to create path for file saves
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

if [ ! -d "(pwd)/athletes/" ]; then
    rm /Users/drewskikatana/Documents/Programming/jiu_jistics/athletes/* #! NOTE: DEPRECIATE AFTER DEPLOYMENT FOR TEST ONLY
    rm /Users/drewskikatana/Documents/Programming/jiu_jistics/logger/* #! NOTE: DEPRECIATE AFTER DEPLOYMENT FOR TEST ONLY
    mkdir "$(pwd)$1"
    mkdir "$(pwd)$2"
    echo -e "${YELLOW}Files will save at $(pwd)$1${NC}"
    echo -e "${YELLOW}Files will log at $(pwd)$2${NC}"
fi
