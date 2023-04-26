def divide():
    try:
        x = int(input("enter x: "))
        y = int(input("enter y: "))
        res=x/y

    except ZeroDivisionError:
        print("ERROR:CANNOT DIVIDE BY ZERO.")
    except ValueError:
        print("ERROR:INVALID INPUT.")
    except Exception as e:
        print("ERROR",e)
    else:
        print("RESULT: ",res)
    finally:
        print("EXECUTION COMPLETE.")

divide()