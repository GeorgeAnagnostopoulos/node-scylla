module.exports = function(datastar, models) {
    
    var cql = datastar.schema.cql;
    var Dog = datastar.define('dogs', {
        ensureTables: true,
        
        schema: datastar.schema.object({
            dog_id: cql.int(),
            group: cql.text(),
            section: cql.text(),
            country: cql.text(),
            dog_name: cql.text(),
        }).partitionKey('dog_id')
    });
    
    return Dog;
}