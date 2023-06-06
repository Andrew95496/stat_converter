# script to create path for file saves
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

if [ ! -d "(pwd)/athletes/" ]; then
    mkdir "$(pwd)/athletes/"
    mkdir "$(pwd)/logger/"
    echo -e "${YELLOW}Files will save at $(pwd)/athletes/${NC}"
fi
