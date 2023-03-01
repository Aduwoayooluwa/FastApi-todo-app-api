from fastapi import FastAPI

app = FastAPI()

todo_list = []


@app.get('/all_todos')
def get_todos():
    return todo_list


@app.post('/add_todo')
def add_todo(todo_item):
    todo_list.append(todo_item)
    return {"message": "Todo Created"}


@app.delete('/delete_todo')
def del_todo(todo_item):
    if todo_item in todo_list:
        todo_list.remove(todo_item)

    else:
        return f"Error: Not Found"

    return {"message": "Todo Deleted"}


@app.put('/update_todo')
def update_todo(todo_item, todo_update):
    todo_item_index = todo_list.index(todo_item)
    print(todo_item_index)
    if todo_item in todo_list:
        todo_list.insert(todo_item_index, todo_update)
        todo_list.remove(todo_item)

    return {"message": "todo list updated"}

