<template>
  <div class="cotnainer">
    <div class="mt-6 view-p">
      <div class="columns" style="height: 100vh;">
        <div class="column is-one-third">
          <div class="box" style="height: 100vh;">
            <Button label="Inbox" icon="pi pi-inbox" iconPos="right" />
            <hr />
            <div v-for="message in user.inbox" :key='message.id'
              id="msg-card-0"
              data-preview-id="0"
              class="card is-msg has-attachment is-active"
              @click.prevent="fetchInbox(message.sender_id)"
            >
              <div class="card-content">
                <div class="msg-header">
                  <span class="msg-from">
                    <p class="has-text-left">From: <a>@{{message.comapny_name}}</a></p>
                  </span>
                  <span class="msg-attachment">
                    <p class="has-text-right"><i class="pi pi-envelope" /></p>
                  </span>
                  <p class="has-text-right msg-timestamp">oct 23 2018</p>
                </div>
                <div class="msg-subject">
                  <p class="has-text-left">
                    <i class="pi pi-star" /> <strong>Hey there</strong>
                  </p>
                </div>
                <div class="msg-snippet">
                  <p class="has-text-left">
                    {{message.body}}
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="column is-half">
          <div class="box">
            <div v-if='chat.chat' class="box message-preview">
              {{chat.chat}}
                                <div class="box-inner">
                                    <div class="header">
                                        <div class="avatar">
                                            <img src="assets/img/avatars/dan.jpg" data-demo-src="assets/img/avatars/dan.jpg" alt="" data-user-popover="1" data-target="webuiPopover23">
                                        </div>
                                        <div class="meta">
                                            <div class="name">Dan Walker</div>
                                            <div class="date">oct 23 2018, 01:02pm</div>
                                        </div>
                                        <div class="meta-right">
                                            <div>
                                                <span class="tag is-important">Important</span>
                                            </div>
                                            <div>
                                                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-paperclip"><path d="M21.44 11.05l-9.19 9.19a6 6 0 0 1-8.49-8.49l9.19-9.19a4 4 0 0 1 5.66 5.66l-9.2 9.19a2 2 0 0 1-2.83-2.83l8.49-8.48"></path></svg>
                                                <small>2 attachments</small>
                                            </div>
                                        </div>
                                    </div>

                                    <hr>
                                    <div class="content">
                                        <p>Hi there!</p>
                                        <p>Corporis tempora id quae fuga. Perspiciatis quam magnam dolores ut quia. Neque vero non laudantium
                                            animi omnis qui debitis minus molestias. Est ut minus est dolores quo harum illum suscipit cumque.
                                        </p>
                                        <p>Natus vel ipsam suscipit est possimus qui quia. Distinctio aspernatur quia tenetur harum. Tempore qui
                                            aut ratione earum quia nam. Et asperiores officiis delectus. Optio quisquam nulla. </p>
                                        <p>Sincerely, <br>Dan.</p>
                                    </div>
                                    <div class="has-text-right">
                                        <a class="button is-solid grey-button is-bold raised">Reply to Message</a>
                                    </div>
                                </div>
                            </div>
          </div>
        </div>
        <div class="column">
          No gap
        </div>
        <div class="column">
          No gap
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import UserWork from "@/modules/user.ts";
import {ref, reactive} from 'vue';
import axios from 'axios';

interface Message {
  body: string,
  timestamp: string;
}

interface Chat {
  chat: [Message]
}

export default {

  setup() {
   const {user} = UserWork()


   const chat = ref<Chat>({ chat: [{} as Message] })

   const fetchInbox = (senderId: number) => {
     axios
     .post('http://127.0.0.1:8000/users/inboxf', {sender: senderId} )
     .then((response) => {
    
     for (const obj of response.data) {
       chat.value.chat.push({body: obj.body, timestamp:'alooo'})
       
     }
       
     })
   }


   return {
     user,
     fetchInbox,
     chat
   }


   }
};
</script>

<style scoped>
.card {
  position: relative;
  margin-bottom: 1.5rem;
  border: 1px solid #e8e8e8;
  border-top-color: rgb(232, 232, 232);
  border-right-color: rgb(232, 232, 232);
  border-bottom-color: #318c63;
  border-left-color: rgb(232, 232, 232);
  color: #4a4a4a;
  max-width: 100%;
  overflow: hidden;
}
</style>
