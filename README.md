
# Exchange Rate App

An app build using the Django Python framework to evaluate Exchange Rate of currencies.


## Aim of the app
The challenge was to develop an app that provides the latest and historical exchange rate for the currency.

App is developed to do basically 2 things:

    1. Get the latest exchange rate of a currency against another currency. 
       Like how is 1 USD equal to INR currently.
![Latest ER](https://user-images.githubusercontent.com/10030091/213785188-fd896112-afc6-4f68-8cad-7e1a30d59504.png)

    2. It provides the historical exchange rate of most currencies against USD
       on a particular date.
 ![Screenshot from 2023-01-22 17-02-28](https://user-images.githubusercontent.com/10030091/213913575-b6a7cd23-40d9-41d4-849d-c6309854ff33.png)
       
## Description of the app
    1. The solution is full-stack with both back-end and front-end being packaged in one single code base.
    2. The reasoning for the choice of Python and Django framework to implement the solution are as follows:
        i. Pyhton is being used as it is easy to understand language and also becomes easy for other team members to 
        contribute with minimum basic knowledge. Also since Python is one of most widely used programming language, it
        has a huge community alongside which is helpful when you are stuck.
        ii. When choice of Python is made, the decision to use Django isn't a hard one to make. Alongside it have several
        added advantages viz. all-inclusive features & functionality; compatibility with ranges of Python libraries;
        scalability; community; security and faster development cycles.
    3. Trade-offs made while implementing the solution:
        i. UI/UX part could have been done better in term of asthetic and look of the website
        ii. As per user experience, could have added a graph which shows rate in a date range
    4. TODOs in the code:
        i. When getting Latest Exchnage rate, the values in UI of base and target currency resets, that should be handled.
        ii. Test cases should be included but since there is not much functionality I have skipped it.
        iii. On the tab in right op corner, the current tab should be highlighted.
        iv. In historical data, user should maximum be able to select previous day date.
        v. There could be a link to get latest exchange rate when viewing the historical data.
        vi. Similarly there could be a link to hsitorical data when viewing latest data.
        vii. The historical data could shown with a beautiful UI, that we generally when when we Google it.
        viii. There could be an option to select mutiple currencies when getting both historical and latest data.


## Deploy app
Follow the steps as listed to get the app up and running.
* Clone the repo
  ```sh
  git clone https://github.com/utkarshdeep/exchangerateapp.git
  ```
* Ensure that Pyhon 3 is installed. If not, [see how to install Pyhton 3](https://docs.python-guide.org/starting/install3/linux/)

* Install the required packages using requirements.txt file
  ```sh
  cd exchnagerateapp/
  pip3 install -r requirements. txt 
  ```
* Create a .env file which looks like .env.exmaple file
  ```sh
  mv .env.exmaple .env
  ```
* Run the following command to start the server
  ```sh
  python3 manage.py runserver
  ```
  
* Go to link to see the app
  ```sh
  http://127.0.0.1:8000/
  ```
  

