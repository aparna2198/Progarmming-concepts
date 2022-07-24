import asyncio
# coroutines
# they are computer program components that generalize subroutines for non preemptive multitasking by allowing execution to be suspended and resumed

async def main():
    print("main func")
    await func("awaiting...")
    print("done")

async def func(text):
    print(text)
    await asyncio.sleep(1)
# event loop is a programming construct or design pattern that waits for and dispatches events or messages in a program.

asyncio.run(main())
# output: 
# main func
# awaiting...
# done

# do something when sleep function is called
async def main():
    print("async method")
    task = asyncio.create_task(func("awaiting..."))
    # await task #this line will wait func to execute and wont go to next line 
    print("done")

async def func(text):
    print(text)
    await asyncio.sleep(1) 

asyncio.run(main())

# output:
# async method
# done
# awaiting...

# add delay in main function 
print("***** add delay in main function *******")
async def main():
    print("async method")
    task = asyncio.create_task(func("delays..."))
    await asyncio.sleep(0.1)
    print("done")

async def func(text):
    await asyncio.sleep(0.1) 
    print(text)
    await asyncio.sleep(10) 

asyncio.run(main())

# output:
# async method
# awaiting...
# done

# understand core concept for asyncio

async def fetch_data():
    print('start fetching')
    await asyncio.sleep(2)
    print('done fetching')
    return {"data":1}

async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)


async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())
    value = await task1
    print(value)
    await task2
 
asyncio.run(main())

# note: as soon as there is delay the other functions (task) starts executing giving the processing power hence you see 8 and 9 of task 2
# prints later because the delay in in task2 when delay is introcued of 0.25 seconds task 1's delay of 2 seconds is done already hence it prints done fetching and data and then controls moves back to task 2 as we are awaitin task 2
# if you need a value from asynchronous function you should await it 