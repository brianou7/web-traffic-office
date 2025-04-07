import graphene

from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.converter import convert_choices_to_named_enum_with_descriptions
from graphene_django.filter import DjangoFilterConnectionField

from vehicles.models import Vehicle
from .models import Violation, Infraction


class VehicleType(DjangoObjectType):

    extra_field = graphene.String()

    def resolve_extra_field(self, info):
        return 'This field is added intentionally to show this GraphQL type can have extra fields'

    class Meta:
        model = Vehicle
        # fields = ('id', 'type', 'license_plate', 'brand', 'model', 'year', 'since', 'owner')
        fields = '__all__'


class InfractionNode(DjangoObjectType):

    class Meta:
        model = Infraction
        # fields = ('id', 'category', 'code', 'description', 'fine', 'impound', 'violations')
        fields = '__all__'
        filter_fields = ['category', 'code', 'description', 'fine', 'impound']
        interfaces = (relay.Node, )

        # convert_choices_to_enum = []


class ViolationNode(DjangoObjectType):

    class Meta:
        model = Violation
        # fields = ('id', 'infraction', 'created_by', 'created_at', 'officer', 'vehicle')
        fields = '__all__'
        filter_fields = {
            'created_by': ['exact'],
            'infraction__code': ['exact'],
            'vehicle__license_plate': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node, )

    @classmethod
    def get_queryset(cls, queryset, info):
        # if not info.context.user.is_anonymous:
        #     return queryset.filter(...)

        return queryset


class Query(graphene.ObjectType):

    infractions = relay.Node.Field(InfractionNode)
    all_infractions = DjangoFilterConnectionField(InfractionNode)

    violations = relay.Node.Field(ViolationNode)
    all_violationss = DjangoFilterConnectionField(ViolationNode)

# class Query(graphene.ObjectType):

#     infractions = graphene.List(InfractionNode)
#     violations = graphene.List(ViolationNode)

#     infraction_by_code = graphene.Field(InfractionNode, code=graphene.String(required=True))

#     def resolve_infractions(root, info):
#         # We can easily optimize query count in the resolve method
#         # return Infraction.objects.select_related('infraction').all()
#         return Infraction.objects.all()

#     def resolve_violations(root, info):
#         return Violation.objects.select_related('infraction').all()

#     def resolve_infraction_by_code(root, info, code):
#         try:
#             return Infraction.objects.get(code=code)
#         except Infraction.DoesNotExist:
#             return None


class CreateInfraction(graphene.Mutation):

    class Arguments:
        category = graphene.String(required=True)
        code = graphene.String(required=True)
        description = graphene.String(required=True)
        fine = graphene.Int(required=True)
        impound = graphene.Boolean(required=True)

    infraction = graphene.Field(InfractionNode)

    @classmethod
    def mutate(cls, root, info, category, code, description, fine, impound):
        infraction = Infraction(
            code=code,
            category=category,
            description=description,
            fine=fine,
            impound=impound
        )
        infraction.save()

        return CreateInfraction(infraction=infraction)


class Mutation(graphene.ObjectType):

    create_infraction = CreateInfraction.Field()
    # update_infraction = UpdateInfraction.Field()
    # delete_infraction = DeleteInfraction.Field()