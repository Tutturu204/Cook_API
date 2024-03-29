from flask import request
from flask_restful import Resource
from http import HTTPStatus

from models.recipe import Recipe
from extensions import db
from flask_jwt_extended import jwt_optional, get_jwt_identity, jwt_required


class RecipeListResource(Resource):
    def get(self):
        data = []
        recipes = Recipe.query.filter_by(is_publish=True).all()
        for i in recipes:
            data.append(i.data)
        return {"data": data}, HTTPStatus.OK

    @jwt_required
    def post(self):
        data = request.get_json()

        current_user = get_jwt_identity()

        recipe = Recipe(name=data["name"],
                        description=data["description"],
                        num_of_servings=data["num_of_servings"],
                        cook_time=data["cook_time"],
                        directions=data["directions"],
                        user_id=current_user
                        )

        recipe.save()

        return recipe.data, HTTPStatus.CREATED


class RecipeResource(Resource):

    @jwt_optional
    def get(self, recipe_id):
        recipe = Recipe.get_by_id(recipe_id)

        current_user = get_jwt_identity()
        if recipe:
            if current_user != recipe.user_id:
                return {"message": "Access is not allowed"}, HTTPStatus.FORBIDDEN
            return recipe.data, HTTPStatus.OK
        else:
            return {"message": "recipe not found"}, HTTPStatus.NOT_FOUND


    @jwt_required
    def put(self, recipe_id):
        recipe = Recipe.get_by_id(recipe_id)

        if recipe:

            current_user = get_jwt_identity()

            if current_user != recipe.user_id:
                return {"message": "Access is not allowed"}, HTTPStatus.FORBIDDEN

            data = request.get_json()

            recipe.name = data["name"]
            recipe.description = data["description"]
            recipe.num_of_servings = data["num_of_servings"]
            recipe.cook_time = data["cook_time"]
            recipe.directions = data["directions"]

            recipe.save()

            return recipe.data, HTTPStatus.OK
        return {"message": "recipe not found"}, HTTPStatus.NOT_FOUND

    @jwt_required
    def delete(self, recipe_id):
        recipe = Recipe.get_by_id(recipe_id)
        if recipe:
            current_user = get_jwt_identity()
            if current_user != recipe.user_id:
                return {"message": "Access is not allowed"}, HTTPStatus.FORBIDDEN

            recipe.delete()
            return {}, HTTPStatus.OK

        return {"message": "recipe not found"}, HTTPStatus.NOT_FOUND


"""
class RecipePublishResource(Resource):
    
    def put(self, recipe_id):
        for recipe in recipe_list:
            if recipe.id == recipe_id:
                recipe.is_publish = True
                return {}, HTTPStatus.OK
        return {"message": "recipe not found"}, HTTPStatus.NOT_FOUND

    
    def delete(self, recipe_id):
        for recipe in recipe_list:
            if recipe.id == recipe_id:
                recipe.is_publish = False
                return {}, HTTPStatus.OK
        return {"message": "recipe not found"}, HTTPStatus.NOT_FOUND
"""