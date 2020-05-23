from django_cron import CronJobBase, Schedule

from api.models import Post


class ResetPostsUpvotes(CronJobBase):
    """Cron job for resetting upvotes count for all posts"""

    RUN_AT_TIMES = ["2:30"]

    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = "news_board.reset_post_upvotes"

    def do(self):
        """Get all posts with upvotes and reset upvotes count"""

        Post.objects.filter(amount_of_upvotes__gt=0).update(
            amount_of_upvotes=0
        )
