# moonbook

Moonboard book creator

## Disclaimer

> This script was basically created to learn how to manipulate images using Python. 

## Usage 

Install dependencies

```sh 
$ pip install -r requirements.txt
```

Create a `config.py` file with the Cookie value for your Moonboard session:

```py 
cookie_header = {
    "Cookie": "__RequestVerificationToken=[...]"
    }
``` 

And run the program:

```log
$ python moonbook.py 
2024-02-07 18:58:33.323848 - 1/409 - 9CIRCLE
2024-02-07 18:58:40.140476 - 2/409 - A WOK TO REMEMBER
2024-02-07 18:58:46.515994 - 3/409 - ARBOR’S BLUE BRUSH
2024-02-07 18:58:53.360699 - 4/409 - ARTHRITIS
2024-02-07 18:59:00.673139 - 5/409 - BEST BALL
[...]
2024-02-07 19:44:45.910383 - 406/409 - AR MOONBOARD MASTERS 2019
2024-02-07 19:44:52.496927 - 407/409 - KUSHNIR
2024-02-07 19:44:57.993833 - 408/409 - ROCKABYE BABY
2024-02-07 19:45:04.615093 - 409/409 - THE ART OF THE MOMENT
```

That will generate a Markdown file. Sample can be seen in [`Moonbook.md`](Moonbook.md)