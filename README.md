# fakerweb
### What the f is this?
 - Random data generator based on the configuration sent via Get Request
 
***
#### Sample Payload

```
  {
      "client_name":{
          "entity": "name",
          "fname_only": false,
          "prefix": "female"
      },
      "client_address":{
          "entity": "address"
      },
      "contract_name":{
          "entity":"text",
          "string_type":"paragraph",
          "prefix":"",
          "suffix":"",
          "upper":false

      }
  }
```
#### Sample Return:
  ```
{
  "client_name": "Connie Dyer",
  "client_address": "7936 Stevens Neck New Kristenshire, LA 58773",
  "contract_name": "Main report recent everybody describe. Author current sound the message reason. World society area account."
}
```


### Why?
 - I need something to generate random data for API testing. Currently API client im using sucks on random data generation

### How to run?
 - clone this repos
 - cd to project directory
 - docker build -t fakerweb .
 - docker run -it --network host --name fakerweb fakerweb (default port :3001 )
 
### Something you dont understand?
 - Daddy chill , im still working in it :)
