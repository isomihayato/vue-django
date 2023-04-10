<template>
    <v-container>
      <v-card-title class="headline text-center mb-5">ToDoList</v-card-title>
      <v-card-text>
        <v-list>
          <v-list-item v-for="item in todoList" :key="item.id">
            <v-list-item-action>
              <v-icon v-if="item.completed" @click.stop="toggleCompleted(item.id)">
                mdi-check
              </v-icon>
              <v-icon v-else @click.stop="toggleCompleted(item.id)">
                mdi-checkbox-blank-outline
              </v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-row>
                <v-col>
                  <v-list-item-title
                    :class="{ 'text-decoration-line-through': item.completed }"
                  >
                    {{ item.title }}
                  </v-list-item-title>
                </v-col>
                <v-col align="left">
                  <v-btn @click="deleteItem(item.id)">delete</v-btn>
                </v-col>
              </v-row>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-card-text>
      <v-card-action>
        <v-form @submit.prevent="addItem">
          <v-text-field v-model="newItem" label="New Item" />
        </v-form>
      </v-card-action>
    </v-container>
</template>

<script>
import axios from "axios";

export default {
  data: () => ({
    todoList: [],
    newItem: "",
  }),
  mounted() {
    axios.get("http://127.0.0.2:8000/api/todo/").then((res) => {
      this.todoList = res.data;
      console.log("status:",res.status)
      console.log("axiosGetData:",res.data)
    })
  },
  methods: {
    toggleCompleted(id) {
      const item = this.todoList.find((item) => item.id === id);
      item.completed = !item.completed;
      axios.put(`/api/todo/${id}/`, item).then(() => {
        console.log(`Item ${id} updated`);
      });
    },
    addItem() {
      axios
        .post("http://127.0.0.2:8000/api/todo/create/", { text: this.newItem, done: false })
        .then((res) => {
          console.log(`Item ${res.data.id} added`);
          this.todoList.push(res.data);
          this.newItem = "";
        });
    },
    deleteItem(id) {
      axios.delete(`/api/todo/${id}/`).then(() => {
        console.log(`Item ${id} deleted`);
        const index = this.todoList.findIndex((item) => item.id === id);
        this.todoList.splice(index, 1);
      });
    },
  },
};
</script>