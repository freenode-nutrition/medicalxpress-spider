# medicalxpress-spider
**medicalxpress-spider** is an article URL and title gatherer for [Medical Xpress](https://medicalxpress.com/).
The most recently scraped data exists in the repository as [**`./data/articles.csv`**](./data/articles.csv).

## Generation
Using a Python 3.7 virtual environment, install the requirements:

    pip install -Ur requirements.in

To generate a data file, run:

    cd ./spider
    ./spider.sh
    
The above script first deletes the preexisting data file, and then generates a new one having the same name.
