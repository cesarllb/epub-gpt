
if __name__ =='__main__':
    from api import app
    import uvicorn
    
    try:
        uvicorn.run(
                app, 
                host= '127.0.0.1', 
                port= 8091,
                )
    except Exception as e:
        print(e)