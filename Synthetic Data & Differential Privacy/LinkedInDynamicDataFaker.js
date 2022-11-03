import { faker } from '@faker-js/faker';

for (var i = 0; i < 30; i++) {
    var record1 = {
        Full_Name:
            faker.name.fullName()
        ,

        Email_Address:
            faker.internet.email()
        ,

        Company:
            faker.company.name()
        ,
        Position:
            faker.name.jobTitle()
        ,
        Connected_On:
            faker.date.between('2015-01-01T00:00:00.000Z', '2022-09-12T00:00:00.000Z')
            };

    var json = JSON.stringify(record1);
    console.log(json);
    