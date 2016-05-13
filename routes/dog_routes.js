module.exports = function(app, datastar) {

    var Dog = require('../models/models.js')(datastar).Dog;
    
    /* Create */
    app.post('/dog', function (req, res) {
        var newDog = new Dog(req.body);
        Dog.create(newDog, function(err) {
            if (err) {
                return res.json({msg: 'error during dog create', error: err});
            };
            res.json({msg: 'dog created successfully'});
        });
    });

    /* Read */
    app.get('/dog', function (req, res) {
        Dog.findAll({}, function(err, dogs) {
            if (err) {
                res.json({msg: 'error during find dogs', error: err});
            };
            res.json({msg: 'dogs found successfully', payload: dogs});
        });
    });

    app.get('/dog/:id', function (req, res) {
        Dog.findOne({dog_id: req.params.id}, function(err, dog) {
            if (err) {
                return res.json({msg: 'error during find dog', error: err});
            };
            if (dog) {
                res.json({msg: 'dog found successfully', payload: dog});
            } else {
                res.json({msg: 'dog not found'});
            }
        });
    });

    /* Update */
    app.put('/dog/:id', function (req, res) {
        Dog.findOne({dog_id: req.params.id}, function(err, dog) {
            if (err) {
                return res.json({msg: 'error during find dog', error: err});
            };
            if (dog) {
                Dog.update({previous: dog, entity: req.body}, function(err) {
                    if (err) {
                        return res.json({msg: 'error during dog update', error: err});
                    };
                    res.json({msg: 'dog updated successfully'});
                });
            } else {
                res.json({msg: 'dog not found'});
            }

        });
    });

    /* Delete */
    app.delete('/dog/:id', function (req, res) {
        Dog.remove({dog_id: req.params.id}, function(err) {
            if (err) {
                return res.json({msg: 'error during remove dog', error: err});
            };
            res.json({msg: 'dog removed successfully'});
        });
    });


};
