<template>
  <div class="cotnainer">
    <div class="mt-6 view-p">
      {{user.inbox}}
      <div class="columns" style="height: 100%;">
        <div class="column is-one-third">
          <div class="box" style="height: 100vh;">
            <Button label="Inbox" icon="pi pi-inbox" iconPos="right" />
            <hr />
            <div v-for="(message, index) in user.inbox" :key='index'

              id="msg-card-0"
              data-preview-id="0"
              class="card is-msg has-attachment is-active"
              
              @click.prevent="fetchInbox(message.slice(-1)[0].sender_id)"
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
                    {{message.slice(-1)[0].body}}
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="column is-auto">
          <div class="box" v-if='chat.messages.length > 1' style='height: 100vh;'>

<ScrollPanel style="width: 100%; height: 100%;" class='scroller'>


                  
            <div
             class="box message-preview" v-for='chat in chat.messages' :key='chat.id'>
      
                                <div  class="box-inner">
                                  {{chat}}
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
                                        <p>{{chat.body}}
                                        </p>
                                        
                                    </div>
                                    <div class="has-text-right">
                                        <a class="button is-solid grey-button is-bold raised">Reply to Message</a>
                                    </div>
                                </div>
                            </div>
                         </ScrollPanel>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import UserWork from "@/modules/user.ts";
import {ref, reactive, onMounted} from 'vue';
import axios from 'axios';

interface Message {
  body: string,
  timestamp: string;
}

interface Chat {
  messages: [Message]
}

export default {

  setup() {
   const {user, inboxq} = UserWork()
   inboxq(false)
  



   const chat = ref<Chat>({ messages: [{} as Message] })

   const fetchInbox = (senderId: number) => {
     axios
     .post('http://127.0.0.1:8000/users/inboxf', {sender: senderId} )
     .then((response) => {
       chat.value.messages = [{} as Message] 
    
     for (const obj of response.data) {
       chat.value.messages.push({body: obj.body, timestamp:'alooo'})
       
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

.scoller .p-scrollpanel-wrapper {
    border-right: 9px solid #f4f4f4;
}

.scroller .p-scrollpanel-bar {
    background-color: #1976d2;
    opacity: 1;
    transition: background-color .3s;
}

.scoller .p-scrollpanel-bar:hover {
    background-color: #318c63;
}
</style>
