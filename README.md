# medicalxpress-spider
**medicalxpress-spider** is an article URL and title gatherer for [Medical Xpress](https://medicalxpress.com/).
The most recently scraped data exists in the repository as [**`./data/articles.csv`**](data/articles.csv).
It was scraped on 2019-02-24.

Note that the [license](LICENSE) does not apply to the scraped data. It applies only to the remainder of the repository.

## Generation
Using a Python 3.7 virtual environment, first install the requirements:

    pip install -Ur requirements.in

To generate a data file, run:

    cd ./spider
    ./spider.sh
    
The above script first deletes the preexisting data file, and then generates a new one having the same name.
