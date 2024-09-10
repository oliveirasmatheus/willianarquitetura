<template>
  <div>
    <div :class="['alert', alertTypeClass]" role="alert">{{ message }}</div>
    <br/>
  </div>
</template>

<script>
export default {
  props: ['message', 'type'],
  computed: {
    alertTypeClass() {
      return `alert-${this.type}`
    }
  }
};
</script>

<style>

</style>