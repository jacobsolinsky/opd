<template>

        <h2>Sign in</h2>
<form class="form-horizontal formtastic user" novalidate="novalidate" id="new_user" action="/users/sign_in" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="✓"><input type="hidden" name="authenticity_token" value="qD6x6gs8jY4K5AJIZUhT7m4Brq6FWhl4IaV5t4y1WFOT5sFrv1mW9oeNBaSM1Rhdd07bCcG18LbvQGF03Dt9cg==">
<div class="form-group row full-row">
    <label class="col-sm-2 control-label" for="user_email">Email</label>
    <div class="col-sm-6">
        <input autofocus="autofocus" class="form-control" type="email" value="" name="user[email]" id="user_email">
    </div>
</div>

<div class="form-group row full-row">
    <label class="col-sm-2 control-label" for="user_password">Password</label>
    <div class="col-sm-6">
        <input autocomplete="off" class="form-control" type="password" name="user[password]" id="user_password">
    </div>
</div>

<div class="form-group row full-row">
    <div class="col-sm-6 col-sm-offset-2">
        <input name="user[remember_me]" type="hidden" value="0"><input type="checkbox" value="1" name="user[remember_me]" id="user_remember_me"> <label for="user_remember_me">Remember me</label>
    </div>
</div>

<div class="form-group row full-row">
    <div class="col-sm-6 col-sm-offset-2">
        <input type="submit" name="commit" value="Sign in" class="btn btn-primary">
    </div>
</div>
</form>

</template>
<script>
export default {}
</script>
