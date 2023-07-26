#!/usr/bin/node

const request = require('request');
const args = process.argv;

const url = args[2];
request(url, (error, response, body) => {
  if (!error) {
    const tasksCompleted = {};
    body.forEach((todo) => {
      if (todo.completed) {
        if (!tasksCompleted[todo.userId]) {
          tasksCompleted[todo.userId] = 1;
        } else {
          tasksCompleted[todo.userId] += 1;
        }
      }
    });
    console.log(tasksCompleted);
  }
});
