class Crop:
    # Class variable to count total crops monitored across all subclasses
    total_crops = 0

    # Constructor to initialize a crop with a name and area in acres
    def __init__(self, name, acres):
        self.name = name  # Store crop name at the instance level
        self.acres = acres  # Store cultivated area (acres) at the instance level
        Crop.total_crops += 1  # Increment the global crop counter whenever a crop is created

    # Class method to access class-level data like total_crops
    @classmethod
    def get_total_crops(cls):
        return cls.total_crops  # Return the total number of crops created so far

    # Static method to validate soil pH independent of any instance or class state
    @staticmethod
    def validate_soil_ph(ph):
        return 6.0 <= ph <= 7.5  # Return True if pH is in optimal range for many cereals

    # Instance method to estimate yield (placeholder logic for demonstration)
    def estimate_yield(self):
        return self.acres * 1.2  # Simple base yield factor applied to acres


# Define a Wheat subclass that inherits from Crop
class Wheat(Crop):
    # Constructor to include wheat-specific properties like variety
    def __init__(self, name, acres, variety):
        super().__init__(name, acres)  # Initialize base Crop fields (name, acres)
        self.variety = variety  # Store wheat variety (e.g., "Durum")

    # Override estimate_yield to account for wheat-specific yield factor
    def estimate_yield(self):
        base = super().estimate_yield()  # Get the base yield from the parent
        return base * 1.1  # Increase yield slightly for wheat due to variety factor
  
    # Static method to validate wheat seed quality score
    @staticmethod
    def validate_seed_quality(score):
        return 0 <= score <= 100  # Ensure quality score lies between 0 and 100


# Define a Rice subclass that inherits from Crop
class Rice(Crop):
    # Constructor to include irrigation level (0-100)
    def __init__(self, name, acres, irrigation_level):
        super().__init__(name, acres)  # Initialize base Crop fields
        self.irrigation_level = irrigation_level  # Store irrigation level percentage

    # Override estimate_yield to depend on irrigation
    def estimate_yield(self):
        factor = 1.0 + (self.irrigation_level / 200.0)  # Increase yield based on irrigation
        return self.acres * 1.0 * factor  # Calculate yield using irrigation factor

    # Static method to validate irrigation level
    @staticmethod
    def validate_irrigation(level):
        return 0 <= level <= 100  # Irrigation level must be a valid percentage


# Define a Corn subclass that inherits from Crop
class Corn(Crop):
    # Constructor to include hybrid flag
    def __init__(self, name, acres, is_hybrid):
        super().__init__(name, acres)  # Initialize base Crop fields
        self.is_hybrid = is_hybrid  # Store whether corn is hybrid or not

    # Override estimate_yield to depend on hybrid status
    def estimate_yield(self):
        factor = 1.3 if self.is_hybrid else 1.0  # Hybrid corn tends to yield better
        return self.acres * 1.1 * factor  # Calculate yield using hybrid factor

    # Static method to validate acreage input
    @staticmethod
    def validate_acres(acres):
        return isinstance(acres, (int, float)) and acres > 0  # Acres must be positive number


# Example usage section demonstrating all features
w = Wheat("Wheat Plot A", 50, "Durum")  # Create a Wheat instance with name, acres, variety
r = Rice("Rice Field B", 40, 60)  # Create a Rice instance with name, acres, irrigation level
c = Corn("Corn Block C", 30, True)  # Create a Corn instance with name, acres, hybrid flag

print("Total crops:", Crop.get_total_crops())  # Display total crops using class method
print("Soil pH 6.8 valid?", Crop.validate_soil_ph(6.8))  # Validate pH using static method
print("Wheat yield:", w.estimate_yield())  # Show wheat-specific yield calculation
print("Rice irrigation valid? 