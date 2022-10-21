## Fetch Reward 


# The idea

Each users have points in their account. Users are only shown their balance, but for reporting purposes we track their points per
payer. Each transaction contains: payer(string), points(integer), and timestamp(date).


# Get Started



# Spending points

There are two rules for determining what points to spend first:

    Oldest points be spent first (oldest based on transaction timestamp, not the order they're recieved)
    No payer's points to go negative

# Example Routes:

## Get All Transaction

[
    {
        "id": 1,
        "payer": "Soub",
        "points": 0,
        "timestamp": "2022-10-13T01:52:37.820955Z",
        "user": 1
    },
    {
        "id": 2,
        "payer": "Moe",
        "points": 0,
        "timestamp": "2022-10-13T01:52:51.520403Z",
        "user": 1
    },
    {
        "id": 3,
        "payer": "2",
        "points": 0,
        "timestamp": "2022-10-13T12:51:15.730168Z",
        "user": 1
    }
]

## Spend Points

    POST:

    {
        "payer": 1,
        "points": 500
    }

    Response:

    {
        "id": 6,
        "payer": "Joey",
        "points": 300,
        "timestamp": "2022-10-13T14:38:14.254609Z",
        "user": 1
    }