var models = module.exports = function(datastar) {
    return new Models(datastar);
}

function Models(datastar) {
    this.Dog = require('./dog_model')(datastar, this);
}