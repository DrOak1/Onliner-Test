<h2>Test assignment NTEC</h2>

> Python version 3.9

> Install requirements by command
``pip install -r requirements``

> Run tests
> ``pytest test``

<h3>Test case to automate</h3>

| Steps                                                                                                                | Result                                                                                                   |
|----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| Open category 'Mobile Phones'                                                                                        | Mobile catalog opened                                                                                    |
| Find any two phones from first 10 and add they to compare.                                                           | Checkboxes set. Compare link exists                                                                      |
| Set search parameters: price (min, max), screen size (min, max) - equal to max and min parameters of selected phones | Selected phones still displayed. Checkboxes checked                                                      |
| Go to any of selected phones                                                                                         | Phone page opened. Parameters are the same with previous page (OS, screen size , dimension, RAM, memory) |
| Click 'Compare' link                                                                                                 | Two phones have correct info (described in previous step). Two phones not equal with each other          |