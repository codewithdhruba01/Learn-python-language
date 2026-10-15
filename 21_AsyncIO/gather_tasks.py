"""
Chapter 21: AsyncIO Concurrent Tasks & Timeouts
Demonstrates asyncio.gather(), concurrent HTTP/API simulation, and asyncio.wait_for().
"""
import asyncio
import time

# ==========================================
# 1. Simulating Concurrent API Requests
# ==========================================
async def fetch_stock_quote(symbol, latency):
    print(f"Requesting ticker: {symbol}...")
    await asyncio.sleep(latency)
    price_map = {"AAPL": 182.50, "GOOGL": 140.20, "TSLA": 215.80, "MSFT": 405.00}
    price = price_map.get(symbol, 100.0)
    print(f"Received ticker : {symbol} -> ${price}")
    return {"symbol": symbol, "price": price}


async def run_gather_demo():
    print("--- 1. Concurrent Fetching with asyncio.gather() ---")
    start = time.perf_counter()

    # Launching 4 requests concurrently
    results = await asyncio.gather(
        fetch_stock_quote("AAPL", 1.0),
        fetch_stock_quote("GOOGL", 1.5),
        fetch_stock_quote("TSLA", 0.8),
        fetch_stock_quote("MSFT", 1.2),
    )

    print("\nAll Quotes Fetched:")
    for quote in results:
        print(f"  {quote['symbol']}: ${quote['price']}")

    elapsed = time.perf_counter() - start
    print(f"Concurrent time: {elapsed:.2f}s (Max latency ~1.5s instead of sequential 4.5s!)\n")


# ==========================================
# 2. Timeout Handling with asyncio.wait_for()
# ==========================================
async def slow_database_query():
    print("[DB] Executing very slow analytical query...")
    await asyncio.sleep(4.0)
    return "Query result data"


async def run_timeout_demo():
    print("--- 2. Enforcing Timeouts with asyncio.wait_for() ---")
    try:
        # Timeout set to 1.5 seconds, while query takes 4.0 seconds
        result = await asyncio.wait_for(slow_database_query(), timeout=1.5)
        print("Got result:", result)
    except asyncio.TimeoutError:
        print("⚠️ Timeout Error: Query took longer than 1.5 seconds and was safely cancelled!")


async def main():
    await run_gather_demo()
    await run_timeout_demo()

if __name__ == "__main__":
    asyncio.run(main())
