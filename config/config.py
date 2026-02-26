import os
from pathlib import Path
from pydantic import BaseModel,Field

class ModelConfig(BaseModel):
    name: str = "nvidia/nemotron-3-nano-30b-a3b:free"
    temperature: float = Field(default=1, ge=0.0, le=2.0)
    context_window: int = 256_000

class ShellEnvPolicy(BaseModel):
    ignore_default_excludes: bool = False
    exclude_patterns: list[str] = Field(
        default_factory = lambda: ['*KEY*','*TOKEN*','*SECRET*'])
    set_vars: dict[str, str] = Field(default_factory=dict)



class Config(BaseModel):
    model: ModelConfig = Field(default_factory=ModelConfig)
    cwd: Path = Field(default_factory = Path.cwd())
    shell_environment: ShellEnvPolicy = Field(default_factory = ShellEnvPolicy)
    max_turns: int = 100
    developer_instructions: str | None = None
    user_instructions: str | None = None

    debug: bool = False

    @property
    def api_key(self) -> str | None:
        return os.environ.get('API_KEY')
    
    @property
    def base_url(self) -> str | None:
        return os.environ.get('BASE_URL')
    
    @property
    def model_name(self) -> str:
        return self.model.name
    
    @model_name.setter
    def model_name(self, value: str) -> None:
        self.model.name = value
    

    @property
    def temperature(self) -> float:
        return self.model.temperature
    
    @temperature.setter
    def temperature(self, value: float) -> None:
        self.model.temperature = value
    
    def validate(self) -> list[str]:
        errors: list[str] = []
        
        if not self.api_key:
            errors.append('No API key found. SET API_KEY env variable')
        
        if not self.cwd.exists():
            errors.append(f'Working directory does not exists: {self.cwd}')
        
        return errors
        






