#! /usr/bin/python3

from fastapi import FastAPI
import random

app = FastAPI()

@app.get('/')
def root():
  return "hello"

products = {
  "1": {
    "name": "Nice product",
    "available": True
  }
}

@app.get('/cart/add/{productid}')
def addToCart(productid):
  # Check that the product exists
  # Check if the product is available
  # Check that user is logged in
  # Get the product information

  product = {}

  return {
    "success": 1,
    "productID": productid,
    "product": product,
    "message": "Product was added to the cart"
  }

@app.get('/game/start/{gametype}/{username}')
def startgame(username = "King", gametype = "basic"):
  # CHALLENGE:
  # Check that gametype is basic or random,
  # if not send back { "success": 0, "message": "Wrong game type" }
  if gametype not in ["basic","random"]:
    return { "success": 0, "message": "Wrong game type" }
  if username in ["Ville","Vipexi"]:
    return { "success": 0, "message": "This user is banned from the game." }

  gameInformation = {
    "message": "Game has started",
    "gameID": random.randint(0,100000),
    "username": username,
    "gametype": gametype
  }

  return gameInformation

@app.post("/game/drawcards")
def drawCards(cards):
  return { "ok" }

#@app.put("...")
#@app.delete("...")
#@app.copy("...")
