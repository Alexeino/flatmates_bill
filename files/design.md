Title: Flatmates Bill
Description: An application to split bills between flatmates. It takes amount of the bill for a particular period as input and flatmates have to pay for how long they stayed in the flat. It will generate a PDF showing their bill amount, period and name.
Objects: Bill:
            - amount
            - period
         Flatmate:
            - name
            - days_in_house
            - pays(days_in_house,bill.amount)
         PDFReport:
            - filename
            - generate(flatmate1, flatmate2, bill)
