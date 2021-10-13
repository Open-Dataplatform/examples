# Code Examples
This repo contains Python code examples on how to retrieve data from the DataPlatform.

In the folders you will find examples for the specified type.

## General notes

### Configuration of Egress
A egress-url is asked to be specified when configuring the Egress client.

This is done in the **conf.ini** file and added under.

```
[Egress]
url = <egress-url>
```

The url used is the following https://dp-prod.westeurope.cloudapp.azure.com/osiris-egress/. 

This results in filling out the **conf.ini** as follows.
```
[Egress]
url = https://dp-prod.westeurope.cloudapp.azure.com/osiris-egress/
```

### Date ranges
Many endpoints take a **from_date** and **to_date** as arguments.

| from_date        | to_date          | interval                                    |
| ---------------- | ---------------- | ------------------------------------------- |
| 2014-01-01T01:01 | 2014-01-01T01:06 | 2014-01-01T01:01 <= data < 2014-01-01T01:06 |
| 2014-01-01T01    | 2014-01-01T04    | 2014-01-01T01:00 <= data < 2014-01-01T04:00 |
| 2014-01-01       | 2014-01-04       | 2014-01-01T00:00 <= data < 2014-01-04T00:00 |
| 2014-01          | 2014-04          | 2014-01-01T00:00 <= data < 2014-04-01T00:00 |
| 2014             | 2016             | 2014-01-01T00:00 <= data < 2016-01-01T00:00 |

### Horizons given
Some endpoints take a Horizon as argument.

The available Horizons is dependent on the dataset and is demonstrated in the examples given.