from fastapi import APIRouter, HTTPException
from app.models import Issue
from app.data import issues

router = APIRouter()

@router.get("/issues", response_model=list[Issue])
def list_issues():
    return issues

@router.post("/issues", response_model=Issue)
def create_issue(issue: Issue):
    issues.append(issue)
    return issue

@router.get("/issues/{issue_id}", response_model=Issue)
def get_issue(issue_id: str):
    for issue in issues:
        if str(issue.id) == issue_id:
            return issue
    raise HTTPException(status_code=404, detail='Issue not found')

@router.delete('/issues/{issue_id}')
def delete_issue(issue_id: str):
    for index, issue in enumerate(issues):
        if str(issue.id) == issue_id:
            del issues[index]
            return {'detail': 'Issue deleted'}
    raise HTTPException(status_code=404, detail="Issue not found")

