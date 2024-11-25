import ell 
from pydantic import BaseModel, Field
from typing import List


class Subtopic(BaseModel):
    """A subtopic is a high level topic that is part of a subject."""
    name: str = Field(description="**Only** the name of the subtopic")
    description: str = Field(
        description="A brief description of the subtopic and how it relates to the parent subject"
    )
    required: bool = Field(
        description="""True if the subtopic is an absolute requirement for the subject,
            False if it is optional to some degree"""
    )

class SubjectBreakdown(BaseModel):
    """A breakdown of a subject into subtopics."""
    description: str = Field(
        description="""A brief description of the subject, e.g. 'Mathematics' and the 
        subtopics that are part of the subject"""
    )
    subtopics: List[Subtopic] = Field(
        description="""A list (between 2 and 10 items as necessary) of high level
            subtopics that build up to the subject."""
    )

class Mapping(BaseModel):
    """A mapping of dependencies between a list of topics."""
    topic: str = Field(description="The topic name")
    dependencies: List[str] = Field(
        description="A list of topic names that the topic depends on"
    )

class TopicMap(BaseModel):
    """A mapping of dependencies between a list of topics."""
    mapping: List[Mapping] = Field(
        description="""A mapping of dependencies between a list of topics.
        The key is the topic name and the value is the topic name that it depends on. 
        Not all topics will have dependencies."""
    )

@ell.complex(model="gpt-4o-2024-08-06", response_format=SubjectBreakdown)
def generate_subject(subject: str) -> SubjectBreakdown:
    """
    You are a subject generator. Given the name of a subject, you need to return a 
    structured description of the subject and the subtopics that are part of the subject.
    """
    return f"generate a description for the subject {subject}"


@ell.complex(model="gpt-4o-2024-08-06", response_format=TopicMap)
def generate_topic_map(subtopics: List[Subtopic]) -> TopicMap:
    """
    You are a topic map generator. Given a list of subtopics, you need to return a 
    structured description of the dependencies between the subtopics.
    """
    return f"generate a topic map for subtopics {subtopics}"
