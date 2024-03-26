#!/usr/bin/node
// A script that computes the number of tasks completed by user id.
const request = require('request');
const _url = process.argv[2];

request(_url, (err, response) => {
  if (err) {
    console.error(err);
    return;
  }
  const todos = JSON.parse(response.body);
  const completedTasks = {};

  todos.forEach((todo) => {
    if (todo.completed) {
      const userId = todo.userId;
      if (completedTasks[userId]) {
        completedTasks[userId]++;
      } else {
        completedTasks[userId] = 1;
      }
    }
  });

  console.log(completedTasks);
});
