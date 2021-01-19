<template>
<div class="cotnainer">
<div class="mt-6 view-p">
<div class="columns" style='height: 100vh;'>
  <div class="column is-one-third">

          <div class="box" style='height: 100vh;'>
<Button label="Inbox" icon="pi pi-inbox" iconPos="right" />
<hr>
<div id="msg-card-0" data-preview-id="0" class="card is-msg has-attachment is-active">
                                    <div class="card-content">
                                        <div class="msg-header">
                                            <span class="msg-from">
                                                    <p class='has-text-left'>From: <a>@Dan</a></p>
                                                </span>
                                            <span class="msg-attachment">
                                                <p class='has-text-right'><i class='pi pi-envelope'/></p>
                                                </span>
                                            <p class="has-text-right msg-timestamp">oct 23 2018</p>
                                        </div>
                                        <div class="msg-subject">
                                           
                                            <p class='has-text-left'><i class='pi pi-star'/> <strong>Hey there</strong></p>
                                        </div>
                                        <div class="msg-snippet">
                                            <p class='has-text-left'>Corporis tempora id quae fuga. Perspiciatis quam magnam dolores ut quia. Neque vero non laudantium animi omnis qui debitis minus molestias. Est ut minus est dolores quo harum illum suscipit cumque.</p>
                                        </div>
                                    </div>
                                </div>         
 </div>
    
  </div>
  <div class="column is-half">
    <div class="box"></div>
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
import Vue from 'vue'
export default ({
    
})
</script>

<style scoped>
.card {position: relative;
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