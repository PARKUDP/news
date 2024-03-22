import { useState } from 'react';

const TodoList = () => {

    const initialState = [
        {
            task: 'Learn vue.js',
            isCompleted: false
        },
        {
            task: 'Learn React Hook',
            isCompleted: false
        },
        {
            task: 'Learn Gatsby.js',
            isCompleted: false
        },     
    ]

    const [todos, setTodos] = useState(initialState);

    return (
        <div>
            <h1>ToDo List</h1>
        </div>
  );
}

export default TodoList;