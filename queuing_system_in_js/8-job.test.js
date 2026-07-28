import createPushNotificationsJobs from './8-job.js';
import kue from'kue';
import assert from 'assert';

const queue = kue.createQueue();

describe('createPushNotificationsJobs', () => {

    before(() => {
        queue.testMode.enter();
    });

    after(() => {
        queue.testMode.clear();
        queue.testMode.exit();
    });

    it('display a error message if jobs is not an array', () => {
        assert.throws(
            () => createPushNotificationsJobs({}, queue),
            Error
        );
    });


    it('create two new jobs to the queue', () => {

        const jobs = [
            {
                phoneNumber: '4153518780',
                message: 'hello'
            },
            {
                phoneNumber: '4153518781',
                message: 'world'
            }
        ];

        createPushNotificationsJobs(jobs, queue);

        assert.equal(
            queue.testMode.jobs.length,
            2
        );

        assert.equal(
            queue.testMode.jobs[0].type,
            'push_notification_code_3'
        );
    });

});